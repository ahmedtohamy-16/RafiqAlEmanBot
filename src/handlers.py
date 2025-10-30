# src/handlers.py

from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome! Use /help to see available commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Available commands:\n/start - Start the bot\n/help - Show this help message\n/profile - Setup your profile')

def profile(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please provide your profile information.')

def unknown(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Sorry, I didn\'t understand that command.')

def main() -> None:
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
    
    # Create the Updater and pass it your bot's token
    updater = Updater("YOUR_TOKEN_HERE")
    
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("profile", profile))
    
    # Handle unknown commands
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    # Start the Bot
    updater.start_polling()
    
    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()