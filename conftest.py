from playwright.sync_api import Playwright
import pytest

@pytest.fixture
def set_up(page):
    page.goto("https://playwright.dev/")

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