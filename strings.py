
# Сообщения для команд
INFO_MESSAGE = (
    "Для работы бота необходимо указать e-mail, на который будут пересылаться все отправленные боту файлы и тему сообщения. "
    "Также необходимо указать настройки сервера для отправки e-mail. Если в параметре SMTP_SERVER указать 1 или 2, то бот будет использовать параметры по умолчанию mail/gmail."
)

HELP_MESSAGE = (
    "/start - Регистрация пользователя.\n"
    "/info - Информация о боте.\n"
    "/help - Список доступных команд.\n"
    "/topsecretinfo - Показать все настройки.\n"
    "/changemail - Изменить e-mail.\n"
    "/changesubj - Изменить тему сообщения.\n"
    "/changesmtp - Настроить SMTP-сервер.\n"
    "/changesmtpserver - Изменить только SMTP-сервер.\n"
    "/changesmtpport - Изменить SMTP-порт.\n"
    "/changesmtpuser - Изменить пользователя SMTP.\n"
    "/changesmtplogin - Изменить логин сервера SMTP.\n"
    "/changesmtppass - Изменить пароль сервера SMTP.\n"
    "Просто отправьте файл или изображение, чтобы переслать его на e-mail."
)

TOP_SECRET_INFO_TEMPLATE = (
    "Ваши данные:\n"
    "id: {id}\n"
    "telegram_id: {telegram_id}\n"
    "username: {username}\n"
    "email: {email}\n"
    "subject: {subject}\n"
    "smtp_server: {smtp_server}\n"
    "smtp_port: {smtp_port}\n"
    "smtp_user: {smtp_user}\n"
    "smtp_password: {smtp_password}\n"
    "message_count: {message_count}"
)

SETT_COUNTER_PROMPT = "отправьте:\n" + "0, чтобы обнулить счётчик сообщений;\n" + "1, чтобы отключить или включить счётчик сообщений;\n" + "2, посмотреть текущее значение\n"

COUNTER_UPDATED_MESSAGE = "Счетчик сообщений сброшен, текущее значение: "

COUNTER_ON_MESSAGE = "Счетчик сообщений включен, текущее значение: 1"

COUNTER_OFF_MESSAGE = "Счетчик сообщений отключен"

CHANGE_EMAIL_PROMPT = "Укажите e-mail, на который будут пересылаться файлы:"

EMAIL_UPDATED_MESSAGE = "Готово! e-mail получателя изменён на: "

CHANGE_SUBJECT_PROMPT = "Укажите тему сообщения:"

SUBJECT_UPDATED_MESSAGE = "Готово! Тема сообщения теперь: "

CHANGE_SMTP_PROMPT = "Введите SMTP-сервер (1 - использовать smtp mail.ru, 2 - использовать smtp.gmail.com, или укажите свой сервер):"

CHANGE_SMTP_SERVER_PROMPT = "Отправьте свой SMTP-сервер (например, smtp.mail.ru или smtp.gmail.com):"

CHANGE_SMTP_PROMPT_PASS = ("Отправьте свой SMTP-сервер (например, smtp.mail.ru или smtp.gmail.com), можно сразу указать сервер и порт (smtp.mail.ru:465).\n" +
                           "Или отправьте пароль для выбора SMTP-сервера по умолчанию:")

SMTP_SERVER_UPDATED_MESSAGE = "Готово! Сервер изменён на: "

CHANGE_SMTP_PORT_PROMPT = "Укажите порт SMTP-сервера (например, 465 для mail.ru или 587 для gmail.com). Текущее значение: "

CHANGE_SMTP_PORT_PROMPT2 = "Введите порт SMTP-сервера (например, 465 для mail.ru или 587 для gmail.com):"

SMTP_PORT_UPDATED_MESSAGE = "Готово! Порт изменён на: "

CHANGE_SMTP_USER_PROMPT = "Укажите имя пользователя SMTP-сервера (например, user@mail.ru или user@gmail.com). Текущее значение: "

CHANGE_SMTP_USER_MESSAGE = "Введите логин SMTP-пользователя (например: user@gmail.com):"

SMTP_USER_UPDATED_MESSAGE = "Готово! Имя пользователя изменено на: "

CHANGE_SMTP_PASSWORD_PROMPT = "Укажите пароль SMTP сервера, [для gmail.com и mail.ru можно получить в настройках безопасности (Пароль для приложений)]:"

SMTP_PASSWORD_UPDATED_MESSAGE = "Готово! Пароль SMTP-сервера изменён."

START_MESSAGE = "Добро пожаловать! Укажите e-mail для пересылки файлов:"

EMAIL_PROMPT = "Введите тему сообщения:"

SMTP_SETTINGS_DEFAULT_MAILRU = "Настройки SMTP-сервера установлены по умолчанию (tn.sender@mail.ru). Можно отправлять файлы!"

SMTP_SETTINGS_DEFAULT_GMAIL = "Настройки SMTP-сервера установлены по умолчанию (tn.sender13@gmail.com). Можно отправлять файлы!"

FILE_SENT_MESSAGE = "Файл успешно отправлен на указанный e-mail!"

IMAGE_SENT_MESSAGE = "Изображение успешно отправлено на указанный e-mail!"

VIDEO_SENT_MESSAGE = "Видео успешно отправлено на указанный e-mail!"

AUDIO_SENT_MESSAGE = "Аудио успешно отправлено на указанный e-mail!"

CONTACT_SENT_MESSAGE = "Контакт успешно отправлен на указанный e-mail!"

LOCATION_SENT_MESSAGE = "Геопозиция успешно отправлена на указанный e-mail!"

REGISTRATION_COMPLETE_MESSAGE = "Регистрация завершена! Теперь вы можете отправлять файлы."

REGISTRATION_INCOMPLETE_MESSAGE = "Пожалуйста, завершите регистрацию с помощью команды /start."

SMTP_PORT_ERROR = "Какой-то другой порт"

EMAIL_SEND_SUCCESS_465 = "Сообщение успешно отправлено: 465"

EMAIL_SEND_SUCCESS_587 = "Сообщение успешно отправлено: 587"

EMAIL_SEND_ERROR = "Ошибка отправки email: {error}"

EMAIL_VALIDATION_ERROR = "Указан некорректный e-mail. Попробуйте снова."

NOT_SUPPORT_PORT = "Неподдерживаемый порт SMTP."

VALIDATION_SMTP_REQUEST = "То, что вы отправили не является smtp-сервером!"

VALIDATION_MAIL_REQUEST = "То, что вы отправили не является e-mail!"

VALIDATION_PORT_REQUEST = "То, что вы отправили не является портом, должно быть число!"

