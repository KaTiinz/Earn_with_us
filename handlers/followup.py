from services.database import get_all_users

async def followup_job(context):
    users = get_all_users()
    for user in users:
        await context.bot.send_message(
            chat_id=user["tg_id"],
            text="วันนี้คุณทำภารกิจรายได้หรือยัง? 💸 รีบกลับมาทำภารกิจเพื่อรับโบนัส!"
        )