from pom.home_page_elements import HomePage
from pom.docs_elements import Docs as DocsPage
from playwright.sync_api import Page, Playwright, sync_playwright, expect
import re


def test_docs_page(set_up) -> None:
    page = set_up

    home_page = HomePage(page)
    docs_page = DocsPage(page)

    home_page.get_started_button.click()
    page.wait_for_url("https://playwright.dev/docs/intro")

    # Assert
    expect(docs_page.docs_intro_header).to_be_visible()