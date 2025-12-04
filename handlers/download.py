from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackQueryHandler

async def download_callback(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="ดาวน์โหลดแอปแล้วรับอั่งเปา!\n\nลิงก์ดาวน์โหลด: https://play.google.com/store/apps/details?id=com.gp.bode.th\nโค้ดพิเศษของคุณ: 【JVBK3M】",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ฉันดาวน์โหลดแล้ว", callback_data="download_done")]
        ])
    )

async def download_done_callback(update, context):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        text="เยี่ยม! คุณใส่โค้ดเรียบร้อยแล้ว 🎉\nตอนนี้คุณสามารถชวนเพื่อนหรือทำภารกิจรายวันเพื่อรับโบนัสเพิ่มเติม!"
    )

download_handler = CallbackQueryHandler(download_callback, pattern="download")
download_done_handler = CallbackQueryHandler(download_done_callback, pattern="download_done")