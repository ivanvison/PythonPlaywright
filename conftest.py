from playwright.sync_api import Playwright
import pytest

@pytest.fixture
def set_up(page):
    page.goto("https://playwright.dev/")

    yield page
    page.close()


@pytest.fixture
def docs_set_up(set_up):

    page = set_up

    yield page


# def set_up(playwright: Playwright):
#     # Assess - Given
#     browser = playwright.chromium.launch(headless=True)
#     context = browser.new_context()
# 
#     # Act
#     page = context.new_page()
#     page.goto("https://playwright.dev/")
# 
#     yield page

@pytest.fixture
def set_up_contact_page(page):
    page.goto("https://www.jotform.com/form-templates/preview/31362999175971/classic&nofs")

    yield page
    page.close()

@pytest.fixture
def set_up_contact_page_fill(set_up_contact_page):

    page = set_up_contact_page
    yield page
