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
def update_data_artist(column, data, name):
    response = (
    supabase
    .schema("public")
    .table(f"artists")
    .update({column: data})
    .eq("name", name)
    .execute()
    )
    print(response.data)
    return response

if __name__ == "__main__":
    path = os.environ.get('local_path_linux')
    name = os.listdir(path)
    for artist in name:
        print(artist)



   
