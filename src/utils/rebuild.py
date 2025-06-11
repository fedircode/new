from dotenv import load_dotenv
import os
import requests

load_dotenv()

site_id = os.getenv("NETLIFY_SITE_ID")
token = os.getenv("NETLIFY_TOKEN")

url = f"https://api.netlify.com/api/v1/sites/{site_id}/builds"
headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}
def main():
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Rebuild iniciado exitosamente 🚀")
    else:
        print("Error al iniciar rebuild:", response.status_code)
        print(response.text)

