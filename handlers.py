from telebot import TeleBot
from database import session, User
from data_validation import is_valid_email, is_valid_smtp, is_valid_smtp_port, is_valid_port
from email_utils import send_email
from config import TEMP_FOLDER, ADMIN, SMTP_USER1, SMTP_USER2, SMTP_PASSWORD1, SMTP_PASSWORD2, PASSWORD_FOR_DEFAULT_SMTP
from strings import INFO_MESSAGE, HELP_MESSAGE, EMAIL_UPDATED_MESSAGE, SUBJECT_UPDATED_MESSAGE, SMTP_SERVER_UPDATED_MESSAGE, SMTP_PORT_UPDATED_MESSAGE, SMTP_USER_UPDATED_MESSAGE, SMTP_PASSWORD_UPDATED_MESSAGE, START_MESSAGE, CHANGE_SMTP_USER_MESSAGE, REGISTRATION_COMPLETE_MESSAGE, REGISTRATION_INCOMPLETE_MESSAGE, FILE_SENT_MESSAGE, IMAGE_SENT_MESSAGE, VIDEO_SENT_MESSAGE, EMAIL_PROMPT, CHANGE_EMAIL_PROMPT, CHANGE_SUBJECT_PROMPT, CHANGE_SMTP_PROMPT, CHANGE_SMTP_SERVER_PROMPT, CHANGE_SMTP_PROMPT_PASS, CHANGE_SMTP_PORT_PROMPT, CHANGE_SMTP_USER_PROMPT, CHANGE_SMTP_PASSWORD_PROMPT, CHANGE_SMTP_PORT_PROMPT2, SMTP_SETTINGS_DEFAULT_MAILRU, SMTP_SETTINGS_DEFAULT_GMAIL, VALIDATION_MAIL_REQUEST, VALIDATION_SMTP_REQUEST, VALIDATION_PORT_REQUEST
import os

# Состояния для регистрации
user_states = {}

def register_handlers(bot: TeleBot):


    @bot.message_handler(commands=['info'])
    def info(message):
        bot.send_message(message.chat.id, INFO_MESSAGE)


    @bot.message_handler(commands=['help'])
    def help_command(message):
        bot.send_message(message.chat.id, HELP_MESSAGE)


    # Команда /topsecretinfo
    @bot.message_handler(commands=['topsecretinfo'])
    def top_secret_info(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if user_id == ADMIN:
            passw = str(user.smtp_password)
        else:
            passw = "Only admin"

        bot.send_message(
            message.chat.id,
            "Ваши данные:\n"
            "id: " + str(user.id) + "\n"
            "telegram_id: " + str(user.telegram_id) + "\n"
            "username: " + str(user.username) + "\n"
            "email: " + str(user.email) + "\n"
            "subject: " + str(user.subject) + "\n"
            "smtp_server: " + str(user.smtp_server) + "\n"
            "smtp_port: " + str(user.smtp_port) + "\n"
            "smtp_user: " + str(user.smtp_user) + "\n"
            "smtp_password: " + passw + "\n"
            "message_count: " + str(user.message_count)
        )


    # Команда /changemail
    @bot.message_handler(commands=['changemail'])
    def change_mail(message):
        user_id = message.from_user.id
        username = message.from_user.username
        # Проверяем, есть ли пользователь в базе
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'changemail'
        bot.send_message(message.chat.id, CHANGE_EMAIL_PROMPT)

    # Обработка команды /changemail
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'changemail')
    def set_new_email(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.email = message.text
        session.commit()
        if is_valid_email(message.text):
            user_states.pop(user_id, None)
            bot.send_message(message.chat.id, EMAIL_UPDATED_MESSAGE + str(user.email))
        else:
            user_states[user_id] = 'changemail'
            bot.send_message(message.chat.id, VALIDATION_MAIL_REQUEST)
            bot.send_message(message.chat.id, CHANGE_EMAIL_PROMPT)


    # Команда /changesubj
    @bot.message_handler(commands=['changesubj'])
    def change_subject(message):
        user_id = message.from_user.id
        username = message.from_user.username
        # Проверяем, есть ли пользователь в базе
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'changesubject'
        bot.send_message(message.chat.id, CHANGE_SUBJECT_PROMPT)

    # Обработка команды /changesubj
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'changesubject')
    def set_new_subject(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.subject = message.text
        session.commit()
        user_states.pop(user_id, None)
        bot.send_message(message.chat.id, SUBJECT_UPDATED_MESSAGE + str(user.subject))


    # Команда /changesmtp
    @bot.message_handler(commands=['changesmtp'])
    def change_smtp(message):
        user_id = message.from_user.id
        username = message.from_user.username
        # Проверяем, есть ли пользователь в базе
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'smtp_server_password'
        bot.send_message(message.chat.id, CHANGE_SMTP_PROMPT_PASS)
        session.commit()


    # Команда /changesmtpserver
    @bot.message_handler(commands=['changesmtpserver'])
    def change_smtp_server(message):
        user_id = message.from_user.id
        username = message.from_user.username
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'change_smtp_server'
        bot.send_message(message.chat.id, CHANGE_SMTP_SERVER_PROMPT)

    # Обработка команды /changesmtpserver
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'change_smtp_server')
    def set_new_smtp_server(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_server = message.text
        session.commit()
        if is_valid_smtp(message.text):
            user_states.pop(user_id, None)
            bot.send_message(message.chat.id, SMTP_SERVER_UPDATED_MESSAGE + str(user.smtp_server))
        else:
            user_states[user_id] = 'change_smtp_server'
            bot.send_message(message.chat.id, VALIDATION_SMTP_REQUEST)
            bot.send_message(message.chat.id, CHANGE_SMTP_SERVER_PROMPT)


    # Команда /changesmtpport
    @bot.message_handler(commands=['changesmtpport'])
    def change_smtp_port(message):
        user_id = message.from_user.id
        username = message.from_user.username
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'change_smtp_port'
        bot.send_message(message.chat.id, CHANGE_SMTP_PORT_PROMPT + str(user.smtp_port))

    # Обработка команды /changesmtpport
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'change_smtp_port')
    def set_new_smtp_port(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_port = message.text
        session.commit()
        if is_valid_port(message.text):
            user_states.pop(user_id, None)
            bot.send_message(message.chat.id, SMTP_PORT_UPDATED_MESSAGE + str(user.smtp_port))
        else:
            user_states[user_id] = 'change_smtp_port'
            bot.send_message(message.chat.id, VALIDATION_PORT_REQUEST)
            bot.send_message(message.chat.id, CHANGE_SMTP_PORT_PROMPT + str(user.smtp_port))



    # Команда /changesmtpuser
    @bot.message_handler(commands=['changesmtpuser'])
    def changesmtpuser(message):
        user_id = message.from_user.id
        username = message.from_user.username
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'smtp_user'
        bot.send_message(message.chat.id, CHANGE_SMTP_USER_PROMPT + str(user.smtp_user))


    # Команда /changesmtplogin
    @bot.message_handler(commands=['changesmtplogin'])
    def change_smtp_login(message):
        user_id = message.from_user.id
        username = message.from_user.username
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'change_smtp_user'
        bot.send_message(message.chat.id, CHANGE_SMTP_USER_PROMPT + str(user.smtp_user))

    # Обработка команды /changesmtplogin
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'change_smtp_user')
    def set_new_smtp_user(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_user = message.text
        session.commit()
        if is_valid_email(message.text):
            user_states.pop(user_id, None)
            bot.send_message(message.chat.id, SMTP_USER_UPDATED_MESSAGE + str(user.smtp_user))
        else:
            user_states[user_id] = 'change_smtp_user'
            bot.send_message(message.chat.id, VALIDATION_MAIL_REQUEST)
            bot.send_message(message.chat.id, CHANGE_SMTP_USER_PROMPT + str(user.smtp_user))



    # Команда /changesmtppass
    @bot.message_handler(commands=['changesmtppass'])
    def change_smtp_password(message):
        user_id = message.from_user.id
        username = message.from_user.username
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        user_states[user_id] = 'change_smtp_password'
        bot.send_message(message.chat.id, CHANGE_SMTP_PASSWORD_PROMPT)

    # Обработка команды /changesmtppass
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'change_smtp_password')
    def set_new_smtp_password(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_password = message.text
        session.commit()
        user_states.pop(user_id, None)
        bot.send_message(message.chat.id, SMTP_PASSWORD_UPDATED_MESSAGE)
        

    # Команда /start
    @bot.message_handler(commands=['start'])
    def start(message):
        user_id = message.from_user.id
        username = message.from_user.username

        # Проверяем, есть ли пользователь в базе
        user = session.query(User).filter_by(telegram_id=user_id).first()
        if not user:
            user = User(telegram_id=user_id, username=username)
            session.add(user)
            session.commit()
        # Устанавливаем состояние
        user_states[user_id] = 'email'
        bot.send_message(message.chat.id, START_MESSAGE)
        #bot.reply_to(message, START_MESSAGE)
        #return EMAIL


    # Обработка e-mail
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'email')
    def set_email(message):
        # Обработка email
        #bot.reply_to(message, f"Ваш email: {message.text}")
        #user_states[message.from_user.id] = None  # Сбрасываем состояние
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.email = message.text
        session.commit()
        if is_valid_email(message.text):
            user_states[user_id] = 'subject'
            bot.send_message(message.chat.id, EMAIL_PROMPT)
            # return SUBJECT
        else:
            user_states[user_id] = 'email'
            bot.send_message(message.chat.id, VALIDATION_MAIL_REQUEST)
            bot.send_message(message.chat.id, CHANGE_EMAIL_PROMPT)



    # Обработка темы сообщения
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'subject')
    def set_subject(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.subject = message.text
        session.commit()
        user_states[user_id] = 'smtp_server_password'
        bot.send_message(message.chat.id, CHANGE_SMTP_PROMPT_PASS)


    # Обработка SMTP-сервера
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'smtp_server_password')
    def set_smtp_server(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_server = message.text
        if message.text == PASSWORD_FOR_DEFAULT_SMTP:
            user_states[user_id] = 'smtp_server'
            bot.send_message(message.chat.id, CHANGE_SMTP_PROMPT)
        else:
            if is_valid_smtp(message.text):
                user_states[user_id] = 'smtp_port'
                bot.send_message(message.chat.id, CHANGE_SMTP_PORT_PROMPT2)
            else:
                user_states[user_id] = 'smtp_server_password'
                bot.send_message(message.chat.id, VALIDATION_SMTP_REQUEST)
                bot.send_message(message.chat.id, CHANGE_SMTP_PROMPT_PASS)
        session.commit()

    # Обработка SMTP-сервера
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'smtp_server')
    def set_smtp_server(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_server = message.text
        #session.commit()

        if user.smtp_server == "1":
            user.smtp_server = "smtp.mail.ru"
            user.smtp_port = 465            #587/465
            user.smtp_user = SMTP_USER1
            user.smtp_password = SMTP_PASSWORD1
            #session.commit()
            user_states.pop(user_id, None)
            #user_states[user_id] = None
            bot.send_message(message.chat.id, SMTP_SETTINGS_DEFAULT_MAILRU)
        elif user.smtp_server == "2":
            user.smtp_server = "smtp.gmail.com"
            user.smtp_port = 587            #587/465
            user.smtp_user = SMTP_USER2
            user.smtp_password = SMTP_PASSWORD2
            #session.commit()
            user_states.pop(user_id, None)
            #user_states[user_id] = None
            bot.send_message(message.chat.id, SMTP_SETTINGS_DEFAULT_GMAIL)
        else:
            user_states[user_id] = 'smtp_port'
            bot.send_message(message.chat.id, CHANGE_SMTP_PORT_PROMPT2)
        session.commit()


    # Обработка порта SMTP
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'smtp_port')
    def set_smtp_port(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_port = message.text
        session.commit()
        if is_valid_port(message.text):
            user_states[user_id] = 'smtp_user'
            bot.send_message(message.chat.id, CHANGE_SMTP_USER_MESSAGE)
        else:
            user_states[user_id] = 'smtp_port'
            bot.send_message(message.chat.id, VALIDATION_PORT_REQUEST)
            bot.send_message(message.chat.id, CHANGE_SMTP_PORT_PROMPT2)


    # Обработка SMTP-пользователя
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'smtp_user')
    def set_smtp_user(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_user = message.text
        session.commit()
        if is_valid_email(message.text):
            user_states[user_id] = 'smtp_password'
            bot.send_message(message.chat.id, CHANGE_SMTP_PASSWORD_PROMPT)
        else:
            user_states[user_id] = 'smtp_user'
            bot.send_message(message.chat.id, VALIDATION_MAIL_REQUEST)
            bot.send_message(message.chat.id, CHANGE_SMTP_USER_MESSAGE)


    # Обработка пароля SMTP
    @bot.message_handler(func=lambda message: user_states.get(message.from_user.id) == 'smtp_password')
    def set_smtp_password(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()
        user.smtp_password = message.text
        session.commit()
        #user_states[user_id] = None
        user_states.pop(user_id, None)
        bot.send_message(message.chat.id, REGISTRATION_COMPLETE_MESSAGE)


    # Обработка файлов и изображений
    @bot.message_handler(content_types=['document', 'photo', 'video'])
    def handle_file(message):
        user_id = message.from_user.id
        user = session.query(User).filter_by(telegram_id=user_id).first()

        if not user or not user.email or not user.subject:
            bot.send_message(message.chat.id, REGISTRATION_INCOMPLETE_MESSAGE)
            return

        print(str(message.content_type))

        # Скачиваем файл
        if message.content_type == 'photo':
            # Получаем фото в максимальном качестве
            raw = message.photo[2].file_id
            file_path = os.path.join(TEMP_FOLDER, raw + ".jpg")
            file_info = bot.get_file(raw)
            with open(file_path, 'wb') as f:
                f.write(bot.download_file(file_info.file_path))
        elif message.content_type == 'video':
            # Получаем видео файл
            raw = message.video.file_id
            file_path = os.path.join(TEMP_FOLDER, raw + ".mp4")
            file_info = bot.get_file(raw)
            with open(file_path, 'wb') as f:
                f.write(bot.download_file(file_info.file_path))
        else:
            file_info = bot.get_file(message.document.file_id)
            file_path = os.path.join(TEMP_FOLDER, f"{message.document.file_name}")
            with open(file_path, 'wb') as f:
                f.write(bot.download_file(file_info.file_path))

        # Увеличиваем счетчик сообщений и отправляем email
        user.message_count += 1
        session.commit()
        send_email(user, file_path)

        # Удаляем файл после отправки
        if os.path.exists(file_path):
            os.remove(file_path)

        if message.content_type == 'document':
            bot.send_message(message.chat.id, FILE_SENT_MESSAGE)
        elif message.content_type == 'photo':
            bot.send_message(message.chat.id, IMAGE_SENT_MESSAGE)
        elif message.content_type == 'video':
            bot.send_message(message.chat.id, VIDEO_SENT_MESSAGE)
