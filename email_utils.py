import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from strings import NOT_SUPPORT_PORT
import os


# Функция для отправки e-mail
def send_email(user, file_path):
    try:
        msg = MIMEMultipart()
        #msg['Date'] = formatdate(localtime=True)                    # Кириллица
        #msg['Message-Id'] = make_msgid()                            # Кириллица
        msg['From'] = user.smtp_user
        msg['To'] = user.email
        msg['Subject'] = f"{user.subject}" if user.message_count == 0 else f"{user.subject} {user.message_count}"   #тернарный оператор

        # Прикрепляем файл
        with open(file_path, 'rb') as f:
            part = MIMEApplication(f.read())
            original_file_name = os.path.basename(file_path)
            part.add_header('Content-Disposition', f'attachment', filename=original_file_name)  # Кириллица
            msg.attach(part)                                        # Кириллица

        # Отправляем письмо
        if user.smtp_port == 465:
            with smtplib.SMTP_SSL(user.smtp_server, user.smtp_port) as server:
                #server.ehlo() # необязательный, вызывается login()
                # ssl-сервер не поддерживает или не нуждается в tls, поэтому не вызываем server.starttls()
                server.login(user.smtp_user, user.smtp_password)
                server.sendmail(user.smtp_user, user.email, msg.as_string())
                #server.close()
                server.quit()
                #print("Сообщение успешно отправлено: 465")
        elif user.smtp_port == 587:
            with smtplib.SMTP(user.smtp_server, user.smtp_port) as server:
            #with smtplib.SMTP(user.smtp_server, user.smtp_port) as server:
                server.ehlo()
                server.starttls()
                server.login(user.smtp_user, user.smtp_password)
                server.sendmail(user.smtp_user, user.email, msg.as_string())
                #server.close()
                server.quit()
                #print("Сообщение успешно отправлено: 587")
        else:
            print(NOT_SUPPORT_PORT)
            with smtplib.SMTP_SSL(user.smtp_server, user.smtp_port) as server:
                server.ehlo()
                server.starttls()
                server.login(user.smtp_user, user.smtp_password)
                server.sendmail(user.smtp_user, user.email, msg.as_string())
                #server.close()
                server.quit()
                print("Порт: " + str(user.smtp_port))

    except Exception as e:
        print(f"Ошибка отправки email: {e}")


def send_email_with_text(user, contact_info):
    try:
        # Настраиваем e-mail
        msg = MIMEMultipart()
        msg['From'] = user.smtp_user
        msg['To'] = user.email
        msg['Subject'] = f"{user.subject}" if user.message_count == 0 else f"{user.subject} {user.message_count}"   #тернарный оператор

        # Прикрепляем информацию о контакте
        msg.attach(MIMEText(contact_info, 'plain'))
        # Отправляем письмо
        if str(user.smtp_port) == "465":
            with smtplib.SMTP_SSL(user.smtp_server, user.smtp_port) as server:
                server.login(user.smtp_user, user.smtp_password)
                #server.send_message(msg)
                server.sendmail(user.smtp_user, user.email, msg.as_string())
                # server.sendmail(user.smtp_user, user.email, msg.as_string())
                server.quit()
                print(f"465")
        elif str(user.smtp_port) == "587":
            with smtplib.SMTP(user.smtp_server, user.smtp_port) as server:
                server.ehlo()
                server.starttls()
                server.login(user.smtp_user, user.smtp_password)
                server.send_message(msg)
                # server.sendmail(user.smtp_user, user.email, msg.as_string())
                server.quit()
                print(f"587")
        else:
            with smtplib.SMTP_SSL(user.smtp_server, user.smtp_port) as server:
                server.ehlo()
                #server.starttls()
                server.login(user.smtp_user, user.smtp_password)
                #server.send_message(msg)
                server.sendmail(user.smtp_user, user.email, msg.as_string())
                # server.sendmail(user.smtp_user, user.email, msg.as_string())
                server.quit()
                print(f"Other")

    except Exception as e:
        print(f"Ошибка отправки email: {e}")
