from playwright.sync_api import Page, Playwright, sync_playwright, expect
import re


def test_api_page(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()

    # Click text=Get started
    page = context.new_page()
    # page.set_default_timeout(3000)
    page.goto("https://playwright.dev/")
    page.locator("text=Get started").click()
    page.wait_for_url("https://playwright.dev/docs/intro")

    # Click a[role="button"]:has-text("Node.js")
    page.locator("a[role=\"button\"]:has-text(\"Node.js\")").click()

    # Click text=Python
    page.locator("text=Python").click()
    page.wait_for_url("https://playwright.dev/python/docs/intro")

    # Click text=API testing
    page.locator("text=API testing").click()
    page.wait_for_url("https://playwright.dev/python/docs/api-testing")

    # Click article a:has-text("Writing API Test")
    page.locator("article a:has-text(\"Writing API Test\")").click()
    page.wait_for_url("https://playwright.dev/python/docs/api-testing#writing-api-test")

    assert page.is_visible("text=GITHUB_API_TOKEN")

   # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*#writing-api-test"))