import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27634799"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a33b9a4b4a177ff2ec59d2743a11c4a0")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://firstmong065:BGQoHt83kaIIen52@cluster0.mwmz9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
