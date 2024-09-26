import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Replace with your bot token and group chat IDs
BOT_TOKEN = 'YOUR_BOT_TOKEN'
SOURCE_CHAT_ID = 'SOURCE_GROUP_CHAT_ID'  # Replace with your source group chat ID
TARGET_CHAT_ID = 'TARGET_GROUP_CHAT_ID'  # Replace with your target group chat ID

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_chat.id == SOURCE_CHAT_ID:
        await context.bot.send_message(chat_id=TARGET_CHAT_ID, text=update.message.text)

def main() -> None:
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handler for messages in the source group
    message_handler = MessageHandler(filters.TEXT & filters.Chat(SOURCE_CHAT_ID), forward_message)
    application.add_handler(message_handler)

    application.run_polling()

if __name__ == '__main__':
    main()
