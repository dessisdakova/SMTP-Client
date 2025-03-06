import os

from dotenv import load_dotenv

from functions.send_email import send_email


load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
IMAGE_PATH = os.getenv("IMAGE_PATH")
DOC_PATH = os.getenv("DOC_PATH")


def test_sending_email_with_valid_data_and_image_attachment(emails_for_clean_up):
    subject = "PythonSMTPClient+image"
    emails_for_clean_up.add(subject)

    body = "This email has been sent by Python SMTP Client and contains an image."

    result = send_email(EMAIL, subject, body, IMAGE_PATH)

    assert result is True


def test_sending_email_with_valid_data_and_document_attachment(emails_for_clean_up):
    subject = "PythonSMTPClient+document"
    emails_for_clean_up.add(subject)

    body = "This email has been sent by Python SMTP Client and contains a document."

    result = send_email(EMAIL, subject, body, DOC_PATH)

    assert result is True


def test_sending_email_with_valid_data_without_attachment(emails_for_clean_up):
    subject = "PythonSMTPClient-no-attachment"
    emails_for_clean_up.add(subject)

    body = "This email has been sent by Python SMTP Client and has no attachments."

    result = send_email(EMAIL, subject, body)

    assert result is True


def test_sending_email_with_invalid_subject():
    subject = 123
    body = "This email has been sent by Python SMTP Client."

    result = send_email(EMAIL, subject, body)

    assert result is False


def test_sending_email_with_invalid_body():
    subject = "PythonSMTPClient"
    body = 123

    result = send_email(EMAIL, subject, body)

    assert result is False


def test_sending_email_with_invalid_path_attachment():
    subject = "PythonSMTPClient"
    body = "This email has been sent by Python SMTP Client."
    path = "invalid/path/to/attachment"

    result = send_email(EMAIL, subject, body, path)

    assert result is False
