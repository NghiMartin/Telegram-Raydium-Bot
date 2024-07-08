from telegram.ext import Application, CommandHandler, MessageHandler, filters
from constants import TOKEN
from commands import start_command, help_command, custom_command, all_pools_command, concentrated_pools_command, standard_pools_command
from handlers import handle_message, error

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('all_pools', all_pools_command))
    app.add_handler(CommandHandler('concentrated_pools', concentrated_pools_command))
    app.add_handler(CommandHandler('standard_pools', standard_pools_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
