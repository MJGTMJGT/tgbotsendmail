import re

# Функция для проверки валидности e-mail
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Функция для проверки валидности smtp
def is_valid_smtp(smtp):
    pattern = r'^(smtp\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, smtp) is not None

# Функция для проверки валидности smtp+port
def is_valid_smtp_port(smtp_port):
    pattern = r'^(smtp\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}:\d{1,5}$'
    return re.match(pattern, smtp_port) is not None

# Функция для проверки валидности порта
def is_valid_port(port):
    pattern = r'^\d+$'
    return re.match(pattern, str(port)) is not None

# Функция для поиска телефонных номеров в тексте
def extract_phone_numbers(text):
    # Регулярное выражение для поиска телефонных номеров
    phone_pattern = r'\+?\d{1,3}[-\s]?\(?\d{1,4}?\)?[-\s]?\d{1,4}[-\s]?\d{1,4}[-\s]?\d{1,9}'
    # Находим все совпадения в тексте
    phone_numbers = re.findall(phone_pattern, text)
    # Форматируем найденные номера
    formatted_numbers = [''.join(number) for number in phone_numbers]
    unique_numbers = set(formatted_numbers) # удаляем дубликаты
    return list(unique_numbers)

