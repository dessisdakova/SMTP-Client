import os
from email.message import Message

from dotenv import load_dotenv

from functions.retrieve_email import retrieve_email
from helpers.extract_email_parts import get_sender, get_subject, get_body, get_attachment_name


load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")


def test_retrieving_email_with_image_attachment(clean_up):
    expected_subject = "PythonSMTPClient+image"
    expected_body = "This email has been sent by Python SMTP Client and contains an image."
    expected_image_name = "unicorn.jpg"

    result = retrieve_email(EMAIL, expected_subject)

    assert isinstance(result, Message)
    assert get_sender(result) == EMAIL
    assert get_subject(result) == expected_subject
    assert get_body(result) == expected_body
    assert get_attachment_name(result) == expected_image_name


def test_retrieving_email_with_doc_attachment(clean_up):
    expected_subject = "PythonSMTPClient+document"
    expected_body = "This email has been sent by Python SMTP Client and contains a document."
    expected_doc_name = "blank_doc.docx"

    result = retrieve_email(EMAIL, expected_subject)

    assert isinstance(result, Message)
    assert get_sender(result) == EMAIL
    assert get_subject(result) == expected_subject
    assert get_body(result) == expected_body
    assert get_attachment_name(result) == expected_doc_name


def test_retrieving_email_without_attachment(clean_up):
    expected_subject = "PythonSMTPClient-no-attachment"
    expected_body = "This email has been sent by Python SMTP Client and has no attachments."

    result = retrieve_email(EMAIL, expected_subject)

    assert isinstance(result, Message)
    assert get_sender(result) == EMAIL
    assert get_subject(result) == expected_subject
    assert get_body(result) == expected_body
    assert get_attachment_name(result) is None


def test_retrieving_email_from_invalid_mailbox():
    subject = "PythonSMTPClient-no-attachment"
    mailxox = "InvalidMailBox"

    result = retrieve_email(EMAIL, subject, mailxox)

    assert result is None


def test_retrieving_email_with_non_existent_subject():
    subject = "ThisEmailDoesNotExist"

    result = retrieve_email(EMAIL, subject)

    assert result is None


def test_retrieving_email_with_non_existent_sender():
    email = "invalid@email.com"
    subject = "PythonSMTPClient-no-attachment"

    result = retrieve_email(email, subject)

    assert result is None
