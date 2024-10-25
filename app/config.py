import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Configuration
MODEL = "gpt-4o-mini"
TEMPERATURE = 0.3
MAX_TOKENS = 2000
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
