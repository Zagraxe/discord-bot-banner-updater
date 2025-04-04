import os
import requests
import base64

# Get environment variable
TOKEN = os.getenv("DISCORD_TOKEN")
BANNER_PATH = "IMG_20250404_030139.png"  # Image located in the root directory

# Read and encode image
with open(BANNER_PATH, "rb") as image_file:
    encoded_data = base64.b64encode(image_file.read()).decode('utf-8')

# Format as data URI
data_url = f"data:image/png;base64,{encoded_data}"
url = "https://discord.com/api/v10/users/@me"

# Send PATCH request to update bot banner
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
