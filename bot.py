import os
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# --------------------
# 1) Load ENV
# --------------------
BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "Earn_with_us_ai_bot")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

# --------------------
# 2) Flask App for Webhook
# --------------------
app = Flask(__name__)

# --------------------
# 3) Telegram Bot Handlers
# --------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ยินดีต้อนรับสู่ Earn with us 💰\n\n"
        "พิมพ์ /invite เพื่อดึงลิงก์เชิญเพื่อน"
    )

async def invite(update: Update, context: ContextTypes.DEFAULT_TYPE):
    code = "JVBK3M"
    link = (
        f"โค้ดเชิญเพื่อนพิเศษ【{code}】\n"
        f"รีบไปดาวน์โหลดแล้วรับอั่งเปาได้เลย:\n"
        f"https://play.google.com/store/apps/details?id=com.gp.bode.th"
    )
    await update.message.reply_text(link)

# --------------------
# 4) Build Application
# --------------------
application = ApplicationBuilder().token(BOT_TOKEN).build()

application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("invite", invite))

# --------------------
# 5) Setup Webhook Endpoint
# --------------------
@app.post(f"/webhook")
def webhook():
    json_update = request.get_json()
    update = Update.de_json(json_update, application.bot)
    application.create_task(application.process_update(update))
    return "OK", 200

@app.get("/")
def index():
    return "Bot is running!", 200

# --------------------
# 6) Run Flask (Railway)
# --------------------
if __name__ == "__main__":
    print("Starting bot with webhook...")

    # ตั้ง webhook
    import telegram
    bot = telegram.Bot(BOT_TOKEN)
    bot.delete_webhook()
    bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
