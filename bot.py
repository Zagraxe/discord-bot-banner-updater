import os
import requests
import base64

TOKEN = os.getenv("DISCORD_TOKEN")
BANNER_PATH = "assets/IMG_20250404_030139.png"

with open(BANNER_PATH, "rb") as image_file:
    encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

data_url = f"data:image/png;base64,{encoded_data}"
url = "https://discord.com/api/v10/users/@me"

response = requests.patch(
    url,
    headers={
        "Authorization": f"Bot {TOKEN}",
        "Content-Type": "application/json"
    },
    json={"banner": data_url}
)

print("Status:", response.status_code)
print("Response:", response.text)
