import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "25214632"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "85f9204d557b13f5b336bd67dc073a46")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://firstmong065:BGQoHt83kaIIen52@cluster0.mwmz9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
