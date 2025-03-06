import pytest
from functions.retrieve_email import imap_decorator


def pytest_collection_modifyitems(items):
    """Modifies test items in place to ensure test modules run in a given order."""
    module_order = ["tests.test_sending_email", "tests.test_retrieving_email"]
    module_mapping = {item: item.module.__name__ for item in items}

    sorted_items = items.copy()
    # Iteratively move tests of each module to the end of the test queue
    for module in module_order:
        sorted_items = [it for it in sorted_items if module_mapping[it] != module] + [
            it for it in sorted_items if module_mapping[it] == module
        ]
    items[:] = sorted_items


@pytest.fixture(scope="session")
def emails_for_clean_up():
    """A set to store email subjects that are used for searching criteria in clean up."""
    subjects = set()
    yield subjects


@pytest.fixture(scope="session")
def clean_up(emails_for_clean_up):
    """Delete all sent emails during tests."""
    yield

    @imap_decorator
    def _delete_emails(mail, emails_to_delete):
        mail.select("Inbox")
        for e_subject in emails_to_delete:
            _, data = mail.search(None, f"(SUBJECT \"{e_subject}\")")
            for e_id in data[0].split():
                mail.store(e_id, '+FLAGS', '\\Deleted')
            mail.expunge()
