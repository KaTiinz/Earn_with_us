from telegram.ext import CallbackQueryHandler

async def invite_callback(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="แชร์บอทให้เพื่อนแล้วรับโบนัส!\n\nข้อความแชร์:\nโค้ดเชิญเพื่อนพิเศษ【JVBK3M】\nhttps://t.me/Earn_with_us_ai_bot?start=JVBK3M"
    )

invite_handler = CallbackQueryHandler(invite_callback, pattern="invite")