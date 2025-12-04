import os
import requests

TOKEN = os.environ.get("BOT_TOKEN")
APP_URL = os.environ.get("APP_URL")  # เช่น https://earnwithus-production.up.railway.app

set_webhook_url = f"{APP_URL}/{TOKEN}"

print("Setting webhook to:", set_webhook_url)

resp = requests.get(
    f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={set_webhook_url}"
)

print("Telegram response:", resp.text)
