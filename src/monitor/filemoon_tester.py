import os
import requests
import json
from dotenv import load_dotenv
from src.api import supabase_api as db
load_dotenv()


artistas = db.get_all_data("official", "artistas")

with open("fallas_filemoon.md", "w") as file:
    file.write("")
    file.close()

for artista in artistas:
    print(f"probando artista: {artista['name']}")
    artista_id = artista["artista_id"]
    data_videos = db.get_data_eq("official", "videos", artista_id)
    for video in data_videos:
        # print(video["code_voe"])
        try:
            response = requests.get(f"https://filemoon.to/e/{video['code_filemoon']}")
            if response.status_code != 200:
                with open("fallas_filemoon.md", "a") as file:
                    file.write(f"artista: {artista['name']}, title: {video['title']} code_filemoon: {video['code_filemoon']}\n")
                    file.close()
                print(f"falla en {artista}, {video['code_filemoon']}")
        except Exception as e:
            print(f"ocurrio un error: {e}")

