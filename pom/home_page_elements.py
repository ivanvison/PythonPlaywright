class HomePage:

    def __init__(self, page):
        self.intro_header = page.locator("text=Playwright enables reliable end-to-end testing for modern web apps.")
        self.get_started_button = page.locator("text=Get started")
        


        