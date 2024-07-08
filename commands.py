from telegram import Update
from telegram.ext import ContextTypes
from helpers import handle_baseURL, get_pool_data, extract_pool_details

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting with me! I am a Raydium Bot')

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
