import os

ADMIN = 000000000   #admin tg id

# Токен бота
TOKEN = "0000000000:AAA0Aaa_A0aaA0AAAAa-aA0AaAA0AaaaAAa"    #Bot token

# Настройки базы данных
DATABASE_URL = 'sqlite:///users.db'

# Папка для временных файлов
TEMP_FOLDER = "Temp"
os.makedirs(TEMP_FOLDER, exist_ok=True)

# SMTP-server
SMTP_USER1 = "usermail@mail.ru"
SMTP_PASSWORD1 = "0000000000000000"


SMTP_USER2 = "usermail@gmail.com"
SMTP_PASSWORD2 = "aaaa aaaa aaaa aaaa"
