from telegram.ext import CallbackQueryHandler

async def tasks_callback(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="นี่คือภารกิจรายวันของคุณ:\n1️⃣ ดาวน์โหลดแอป\n2️⃣ แชร์บอท\n3️⃣ ชวนเพื่อน\n\nทำครบทุกข้อเพื่อรับโบนัส!"
    )

task_handler = CallbackQueryHandler(tasks_callback, pattern="tasks")