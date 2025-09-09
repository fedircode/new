import os
from supabase import create_client, Client
import json
import dotenv
import time
import requests
from icecream import ic
from src.api.voe import Voe
from src.api.filemoon import FilemoonAPI as fl
ic.disable()
dotenv.load_dotenv()

# mover cliente en otro archivo, para mas limpieza y reutilización DRY
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(
    url, 
    key,
)
token_voe = os.environ.get("API_KEY_VOE")
token_filemoon = os.environ.get("API_KEY_FILEMOON")

def get_data_db(schema, table, query):
    response = (
        supabase
        .schema(schema)
        .table(table)
        .select(query)
        .execute()
    )
    ic(response.data)
    return response.data

def get_artist_local():
    folders = os.listdir("E:/datos/")
    ic(folders)
    return folders

def get_video_local(folders_local):
    data = {}
    for folder in folders_local:
        path = f"E:/datos/{folder}/videos"
        try:
            videos = os.listdir(path)
            data[folder] = videos
            print(f"📁 {folder}: {len(videos)} videos locales")
        except FileNotFoundError:
            print(f"❌ Carpeta no encontrada: {path}")
            data[folder] = []
    ic(data)
    return data

def insert_data_db(table, query):
    try:
        response = (
            supabase
            .table(table)
            .insert(query)
            .execute()
        )
        ic(response)
    except Exception as e:
        print(e)

def create_json(data):
    with open("data.json", "w") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=False))
        f.close()
    print("JSON file created successfully.")

def update_data_public(table, data, where):
    response = (
        supabase
        .table(table)
        .update(data)
        .eq("title", where)
        .execute()
    )
    return response

def filter_voe_name(token, title):
    """Buscar video específico por título en VOE"""
    url = f"https://voe.sx/api/file/list?key={token}&name={title}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("success") and data.get("result", {}).get("data"):
            videos = data["result"]["data"]
            print(f"🔍 Encontrados {len(videos)} videos para '{title}' en VOE")
            return videos
        else:
            print(f"⚠️  No se encontró '{title}' en VOE")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión buscando '{title}': {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Error decodificando JSON para '{title}': {e}")
        return []

def get_artists_with_videos():
    """Obtener artistas de la BD que coincidan con carpetas locales"""
    artists_db = get_data_db("public", "artists", "name, artist_id")
    folders_local = get_artist_local()
    
    # Crear diccionario para lookup rápido
    artists_dict = {artist["name"]: artist["artist_id"] for artist in artists_db}
    
    # Filtrar solo artistas que existen localmente
    matching_artists = []
    for folder in folders_local:
        if folder in artists_dict:
            matching_artists.append({
                "name": folder,
                "artist_id": artists_dict[folder]
            })
    
    print(f"🎨 Artistas coincidentes: {len(matching_artists)}")
    return matching_artists

def update_all_code_voe():
    print("🚀 Iniciando actualización de códigos VOE...")
    
    # Obtener artistas que coinciden con carpetas locales
    artists = get_artists_with_videos()
    
    # Obtener videos locales de todas las carpetas
    folders_local = get_artist_local()
    videos_local = get_video_local(folders_local)
    
    stats = {
        "processed": 0,
        "updated": 0,
        "not_found_voe": 0,
        "not_found_db": 0,
        "errors": 0
    }
    
    for artist in artists:
        artist_name = artist["name"]
        artist_id = artist["artist_id"]
        
        print(f"\n🎨 Procesando artista: {artist_name}")
        
        if artist_name not in videos_local:
            print(f"⚠️  No hay videos locales para {artist_name}")
            continue
        
        videos = videos_local[artist_name]
        print(f"📹 Videos locales encontrados: {len(videos)}")
        
        for video_file in videos:
            try:
                # Obtener título limpio (sin extensión)
                title = video_file.split('.')[0]
                stats["processed"] += 1
                
                print(f"\n📹 Procesando: {video_file} -> '{title}'")
                
                # Verificar si el video existe en la BD
                db_check = (
                    supabase
                    .table("videos")
                    .select("title, code_voe")
                    .eq("title", title)
                    .eq("artist_id", artist_id)
                    .execute()
                )
                
                if not db_check.data:
                    print(f"⚠️  Video '{title}' no encontrado en BD")
                    stats["not_found_db"] += 1
                    with open("error.log", "a", encoding="utf-8") as f:
                        f.write(f"DB_NOT_FOUND: {title} - {artist_name}\n")
                    continue
                
                # Buscar el video en VOE por título
                voe_videos = filter_voe_name(token_voe, title)
                
                if not voe_videos:
                    print(f"⚠️  Video '{title}' no encontrado en VOE")
                    stats["not_found_voe"] += 1
                    with open("error.log", "a", encoding="utf-8") as f:
                        f.write(f"VOE_NOT_FOUND: {title} - {artist_name}\n")
                    continue
                
                # Tomar el primer resultado (más exacto)
                voe_video = voe_videos[0]
                filecode = voe_video["filecode"]
                # lenght = voe_video["lenght"]
                filesize = voe_video["size"]
                
                print(f"✅ Encontrado en VOE: {voe_video['name']} -> {filecode}")

                # Actualizar lenght en la BD
                # update_lenght_response = update_data_public("videos", {"lenght": lenght}, title)
                
                # update filesize db
                update_filesize_response = update_data_public("videos", {"file_size": filesize}, title)

                if update_filesize_response.data:
                    stats["updated"] += 1
                    print(f"✅ Actualizado en BD: {title}")
                    with open("success.log", "a", encoding="utf-8") as f:
                        f.write(f"SUCCESS: {title} - {artist_name} - {filecode}\n")
                else:
                    print(f"❌ No se pudo actualizar en BD: {title}")
                    stats["errors"] += 1
                
                # Pausa para respetar rate limits
                time.sleep(0.5)
                
            except Exception as e:
                print(f"💥 Error procesando {video_file}: {e}")
                stats["errors"] += 1
                with open("error.log", "a", encoding="utf-8") as f:
                    f.write(f"ERROR: {video_file} - {artist_name} - {str(e)}\n")
    
    # Reporte final
    print("\n" + "="*60)
    print("📊 REPORTE FINAL:")
    print(f"📹 Videos procesados: {stats['processed']}")
    print(f"✅ Videos actualizados: {stats['updated']}")
    print(f"⚠️  No encontrados en VOE: {stats['not_found_voe']}")
    print(f"⚠️  No encontrados en BD: {stats['not_found_db']}")
    print(f"❌ Errores: {stats['errors']}")
    print("="*60)
    print("🏁 Proceso completado!")



if __name__ == "__main__":
    data = (
        supabase
        .table("videos")
        .select("title, views, thumbnail, code_voe, code_filemoon, artists(name)")
        .is_("views", "null")
        .execute()
    )
    data_filter = []
    for item in data:
        if item["thumbnail"] == None and item["views"] == None:
            data_filter.append(item)
    print(data_filter)
            




