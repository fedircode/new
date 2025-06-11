# añadir id carpetas filemoon a la db
#añadir nacionalidad a artistas 
import os
import requests
from dotenv import load_dotenv
from supabase import create_client, Client
from supabase.client import ClientOptions
from src.api import supabase_api as db
from src.api import filemoon as fm
load_dotenv()
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(
    url, 
    key,
    options=ClientOptions(
        schema="official",
    )
)
def update_data_artist(pais, name):
    response = (
    supabase.table(f"artistas")
    .update({"pais": pais})
    .eq("name", name)
    .execute()
    )
    print(response.data)
    return response

if __name__ == "__main__":
    token_filemoon = os.environ.get('API_KEY_FILEMOON')
    folders_filemoon = fm.get_folders_filemoon(token_filemoon)
    artistas_db = db.get_all_data("official", "artistas")
    for artistas in artistas_db:
        update_data_artist("chile", artistas["name"])



   
