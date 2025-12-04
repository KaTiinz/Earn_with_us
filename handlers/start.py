from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CommandHandler
from services.database import save_user

async def start(update: Update, context):
    user = update.effective_user
    save_user(user.id, user.first_name)
    keyboard = [
        [InlineKeyboardButton("🔥 ดาวน์โหลดแอป", callback_data="download")],
        [InlineKeyboardButton("🎁 โค้ดเชิญเพื่อน", callback_data="invite")],
        [InlineKeyboardButton("💸 ภารกิจรายวัน", callback_data="tasks")]
    ]
    await update.message.reply_text(
        "ยินดีต้อนรับสู่ Earn with us! 🚀\nรับรายได้ฟรีทุกวันแบบ passive income!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
start_handler = CommandHandler("start", start)