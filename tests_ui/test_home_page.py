from playwright.sync_api import expect
from pom.home_page_elements import HomePage


def test_home_page(set_up) -> None:
    page = set_up
    home_page = HomePage(page)
    
    # Assert
    expect(home_page.intro_header).to_be_visible()