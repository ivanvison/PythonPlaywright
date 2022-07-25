from pom.contact_page_elements import ContactPage
from playwright.sync_api import Playwright, expect
import pytest


@pytest.mark.smoke
def test_contact_page(set_up_contact_page):
    
    page = set_up_contact_page

    contact_page = ContactPage(page)
    
    expect(contact_page.sub_title).to_be_visible()
    


# this method will combine each name with each email and each message, meaning that will will have 28 test cases
    # @pytest.mark.parametrize("name",["Test Name 1", "Test Name 2", pytest.param("Test Name 3", marks=pytest.mark.xfail)])
    # @pytest.mark.parametrize("email",["test1@testingcorp.com", "test2@testingcorp.com", pytest.param("test3@testingcorp.com", marks=pytest.mark.xfail)])
    # @pytest.mark.parametrize("message",["This is test sample 1", "This is test sample 2", pytest.param("This is test sample 3", marks=pytest.mark.xfail)])

# This method of parametrization will only create 3 test cases
@pytest.mark.parametrize("name, email, message",[("Test Name 1", "test1@testingcorp.com","This is test sample 1"),
                                                ("Test Name 2", "test2@testingcorp.com", "This is test sample 2"),
                                                pytest.param("Test Name 3", "test3@testingcorp.com", "This is test sample 3", marks=pytest.mark.xfail)] )
def test_contact_page_form(set_up_contact_page_fill, name, email, message) -> None:
    # Assess - Given
    page = set_up_contact_page_fill
    contact_page = ContactPage(page)

    # Act
    contact_page.submit_form(name,email,message)

    # Assert
    expect(contact_page.success_message_sent).to_be_visible()

    page.close()

