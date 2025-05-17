from telegram import Update
     from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
     import asyncio

     # توکن ربات
     TOKEN = "8183839514:AAHewCwhlwRa7S9FUU1Zh4aY7ir-fSr_kVg"

     # خواندن کلمات ممنوعه
     with open("bad_words.txt", "r", encoding="utf-8") as file:
         bad_words = [word.strip().lower() for word in file]

     # بررسی و حذف پیام
     async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
         if not update.message or not update.message.text:
             return

         text = update.message.text.lower()
         chat_id = update.message.chat_id
         message_id = update.message.message_id

         for word in bad_words:
             if word in text:
                 try:
                     await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                     print(f"پیام حاوی '{word}' حذف شد.")
                 except Exception as e:
                     print(f"خطا: {e}")
                 break

     # دستور شروع
     async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
         await update.message.reply_text("ربات شروع شد! پیام‌های بد رو پاک می‌کنم.")

     # تابع اصلی
     async def main():
         app = Application.builder().token(TOKEN).build()
         app.add_handler(CommandHandler("start", start))
         app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
         print("ربات در حال اجراست...")
         await app.run_polling()

     if __name__ == "__main__":
         asyncio.run(main())