import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        '🕌 أهلا وسهلا بك في بوت رفيق الإيمان!\n\n'
        'اكتب /help للمزيد من الأوامر'
    )

async def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
/start - ابدأ مع البوت
/help - عرض هذه الرسالة
/quran - آية اليوم
/hadith - حديث اليوم
/prayer - مواقيت الصلاة
/profile - إعدادات حسابك
    """
    await update.message.reply_text(help_text)

async def unknown(update: Update, context: CallbackContext) -> None:
    """Handle unknown commands."""
    await update.message.reply_text('عذراً، لم أفهم هذا الأمر. اكتب /help للمساعدة.')

async def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    # Start the Bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())