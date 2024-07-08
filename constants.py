# Import the necessary module
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

BOT_TOKEN = os.environ['TOKEN']
BOT_USERNAME = os.environ['BOT_USERNAME']