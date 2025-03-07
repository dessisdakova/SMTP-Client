import os

from dotenv import load_dotenv


load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
IMAGE_PATH = os.getenv("IMAGE_PATH")
DOC_PATH = os.getenv("DOC_PATH")

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  # TLS

IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993