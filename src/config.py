import os

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")
    
    # Add any other API configurations here
    API_BASE_URL = os.getenv("API_BASE_URL")
    
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")