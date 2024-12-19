from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL, SMTP_USER1, SMTP_PASSWORD1

# Настройки базы данных
Base = declarative_base()
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    email = Column(String)
    subject = Column(String)
    smtp_server = Column(String, default="smtp.mail.ru")
    smtp_port = Column(Integer, default=465)
    smtp_user = Column(String, default=SMTP_USER1)
    smtp_password = Column(String, default=SMTP_PASSWORD1)
    message_count = Column(Integer, default=1)

def init_db():
    Base.metadata.create_all(engine)
