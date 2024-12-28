from telebot import TeleBot
from config import TOKEN
from handlers import register_handlers
from database import init_db

# Инициализация бота (Настройки бота)
# bot = TeleBot.TeleBot(TOKEN)
bot = TeleBot(TOKEN)

# Инициализация базы данных
init_db()

# Регистрация обработчиков
register_handlers(bot)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
