from pom.contact_page_elements import ContactPage
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.skip(reason="Not ready")
def test_contact_page():
    pass

@pytest.mark.regression
def test_contact_page_form(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Act
    page = context.new_page()
    contact_page = ContactPage(page)
    contact_page.navigate()

    contact_page.submit_form('Test Name', 'testing@tescorp.com', 'Lorem Ipsum Dolor sit amet')

    # Assert
    expect(contact_page.success_message_sent).to_be_visible()

