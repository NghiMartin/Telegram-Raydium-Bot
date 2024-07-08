from telegram import Update
from telegram.ext import ContextTypes
from helpers import handle_baseURL, get_pool_data, extract_pool_details

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = (
        "👋 Welcome to the Raydium Helper Bot!\n\n"
        "I'm here to assist you with everything related to Raydium liquidity pools.\n\n"
        "📊 **Features:**\n"
        "- View all available liquidity pools on Raydium\n"
        "- Check out concentrated liquidity pools\n"
        "- Discover standard liquidity pools\n"
        "- Add liquidity to pools effortlessly\n\n"
        "To get started, use the following commands:\n"
        "- `/all_pools` to view all available pools\n"
        "- `/concentrated_pools` to view concentrated pools\n"
        "- `/standard_pools` to view standard pools\n\n"
        "Let's dive into the world of Raydium! 🌊💰\n\n"
        "Don't forget to follow [Raydium Protocol](https://x.com/RaydiumProtocol), [Superteam DAO](https://x.com/SuperteamDAO), [Fay Nguyen](https://x.com/faynguyen07), and [Venn Luu](https://x.com/vennluu) for the latest updates on blockchain and more! 🚀"
    )
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a Raydium Bot! Please type something so I can respond!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')

async def all_pools_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pool_data = get_pool_data(handle_baseURL('all', 7, 1))
    pool_details = extract_pool_details(pool_data, '✨Top 7 All Pools on Raydium 🔥:')
    pools_info = "\n".join(pool_details)
    await update.message.reply_text(pools_info)

async def concentrated_pools_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pool_data = get_pool_data(handle_baseURL('concentrated', 7, 1))
    pool_details = extract_pool_details(pool_data, '✨ Top 7 Concentrated Pools on Raydium 🔥:')
    pools_info = "\n".join(pool_details)
    await update.message.reply_text(pools_info)

async def standard_pools_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pool_data = get_pool_data(handle_baseURL('standard', 7, 1))
    pool_details = extract_pool_details(pool_data, '✨ Top 7 Standard Pools on Raydium 🔥:')
    pools_info = "\n".join(pool_details)
    await update.message.reply_text(pools_info)
