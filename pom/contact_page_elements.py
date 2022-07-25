
class ContactPage:

    def __init__(self, page):
        self.page = page
        self.sub_title = page.locator("text=Please fill this form in a decent manner")
        self.full_name_input = page.locator("#input_8")
        self.email_input = page.locator("#input_7")
        self.message_input = page.locator("#input_4")
        self.submit_button = page.locator("button[type='submit']")
        self.success_message_sent = page.locator("text=Thank You!")

    def submit_form(self, name, email, message):
        self.full_name_input.fill(name)
        self.email_input.fill(email)
        self.message_input.fill(message)
        self.submit_button.click()

    