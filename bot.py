import os
import requests

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("DISCORD_GUILD_ID")
BANNER_PATH = "assets/banner.png"

with open(BANNER_PATH, "rb") as image_file:
    banner_data = image_file.read()

url = f"https://discord.com/api/v10/guilds/{GUILD_ID}/banner"

response = requests.patch(
    url,
    headers={"Authorization": f"Bot {TOKEN}"},
    files={"banner": ("banner.png", banner_data)}
)

print("Status:", response.status_code)
print("Response:", response.text)
