import os
import telegram
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
from flask import Flask, request

TOKEN = os.environ.get("BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

# --- Handlers ---
def start(update, context):
    update.message.reply_text("ยินดีต้อนรับ! บอททำงานออนไลน์ 24 ชม. ✨")

def echo(update, context):
    user_msg = update.message.text
    update.message.reply_text(f"คุณพิมพ์ว่า: {user_msg}")

# --- Webhook route ---
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

# Dispatcher
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# index
@app.route("/")
def index():
    return "Bot is running on Railway!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
