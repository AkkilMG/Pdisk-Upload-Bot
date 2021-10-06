import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    API_ID = int(os.environ.get("API_ID", 123456))

    API_HASH = os.environ.get("API_HASH", "")
    
    API_KEY = os.environ.get("API_KEY", "")

    # AUTH_USERS = set(str(x) for x in os.environ.get("AUTH_USERS", "").split())

    # PRIVATE = bool(os.environ.get("PRIVATE", ""))

    
