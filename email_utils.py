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
        msg['Subject'] = f"{user.subject} {user.message_count}"

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
                print("Сообщение успешно отправлено: 465")
                print(str(user))
                print(str(file_path))
        elif user.smtp_port == 587:
            with smtplib.SMTP(user.smtp_server, user.smtp_port) as server:
            #with smtplib.SMTP(user.smtp_server, user.smtp_port) as server:
                server.ehlo()
                server.starttls()
                server.login(user.smtp_user, user.smtp_password)
                server.sendmail(user.smtp_user, user.email, msg.as_string())
                #server.close()
                server.quit()
                print("Сообщение успешно отправлено: 587")
        else:
            print(NOT_SUPPORT_PORT)
            with smtplib.SMTP_SSL(user.smtp_server, user.smtp_port) as server:
                server.login(user.smtp_user, user.smtp_password)
                server.sendmail(user.smtp_user, user.email, msg.as_string())
                #server.close()
                server.quit()
                print("Какой-то другой порт")
    except Exception as e:
        print(f"Ошибка отправки email: {e}")
