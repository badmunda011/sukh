# FOR SELF HOST
# EDIT THIS FILE AND RENAME TO config.py TO MAKE THIS BOT WORKING
# FILL THESE VALUES ACCORDINGLY.

from PbxConfig.config import Config


class Development(Config):
    # get these values from my.telegram.org.
    
    APP_ID = 27383453 # 666666 is a placeholder. Fill your 6 digit api id
    API_HASH = "4c246fb0c649477cc2e79b6a178ddfaa"  # replace this with your api hash
    BOT_TOKEN = "7451378287:AAHmSqw8cIDKo4UmImAK2opVQkZIm4ArXjg"  # Create a bot from @BotFather and paste the token here
    BOT_LIBRARY = "telethon"  # fill 'pyrogram' if you want pyrogram version of Pbxbot else leave it as it is.
    DATABASE_URL = "postgres://lwktrpsc:1UlTfWHhnxKZWRETlLu6AF0x4AsyKXhO@rosie.db.elephantsql.com/lwktrpsc"  # A postgresql database url from elephantsql
    PBXBOT_SESSION = "hsjns"  # telethon or pyrogram string according to BOT_LIBRARY
    HANDLER = "®"  # Custom Command Handler
    SUDO_HANDLER = "©"  # Custom Command Handler for sudo users.


# end of required config
# Pbxbot
