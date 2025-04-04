import os
import requests
import base64

# Récupération des variables d'environnement
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
BOT_ID = os.getenv("BOT_ID")
BANNER_PATH = "assets/banner.png"

def encode_image(image_path):
    """Encode une image en base64 pour Discord."""
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def update_banner():
    """Met à jour la bannière du bot sur Discord."""
    if not DISCORD_TOKEN or not BOT_ID:
        print("⚠️ Erreur: DISCORD_TOKEN ou BOT_ID manquant.")
        return

    url = f"https://discord.com/api/v10/users/@me"
    headers = {
        "Authorization": f"Bot {DISCORD_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {"banner": encode_image(BANNER_PATH)}

    response = requests.patch(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("✅ Bannière mise à jour avec succès !")
    else:
        print(f"❌ Erreur ({response.status_code}): {response.text}")

if __name__ == "__main__":
    update_banner()
  
