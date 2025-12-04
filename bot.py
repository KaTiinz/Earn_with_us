import os
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler
from handlers.start import start_handler
from handlers.download import download_handler, download_done_handler
from handlers.invite import invite_handler
from handlers.tasks import task_handler
from handlers.followup import followup_job
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(start_handler)
    app.add_handler(download_handler)
    app.add_handler(download_done_handler)
    app.add_handler(invite_handler)
    app.add_handler(task_handler)
    app.job_queue.run_repeating(followup_job, interval=3600)
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())