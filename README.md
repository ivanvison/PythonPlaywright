Thank you for getting to this point. This repository was created for a project to learn Playwright with Python. "Playwright with Python for Web Automation Testing + Visual" from UDEMY. For this training the instructor also provided a 3hours basic training in Python. Trainer: Symon Storozhenko.

## Topics Covered
- Section 1: Introduction
- Section 2: Environment Setup
- Section 4: Python Fundamentals
- Section 5: Python OOP Basics
- Section 6: Python Modules, Standard Library and Pip
- Section 7: Playwright Basics
- Section 8: Playwright Selectors
- Section 9: Assertions
- Section 10: Waits
- Section 11: POM and Project Structure
- Section 12: Pytest Framework Basics
- Section 13: Reporting and Parallel Execution via CLI
- Section 14: Pytest - Playwright fictures and CLI commands
- Section 15: Data Driven Testing
- Section 16: CI/CD Integration
- Section 17: Authentication Scenarios
- Section 18: Visual Testing


## Install / Usage Process (My personal setup)
1. Installed [VS Code](https://code.visualstudio.com).
2. Installed [Python](https://python.org).
3. Added Environment Variables

### Setting up Environment Variables in Windows 10 PRO x64

**Prerequisites:**
- Python
- The path to `python.exe`, usually `C:\Users\Ivan\AppData\Local\Programs\Python\Python310\`

1. Press Start > Write `environment` > Click `Edit the system variables environment`
2. Click Environment Variables
3. Under System variables, click New
    - Variable Name = python
    - Variable Value = C:\Users\Ivan\AppData\Local\Programs\Python\Python310\
4. Ok > Ok

## Notes from the training per section

### Section 4: Python Fundamentals
- Annotations: way to associate arbitrary expressions to function arguments and return values. Basically to specify WHAT exactly is expected
- def sample(a: int, b: int) -> int:


### Section 6: Python Modules, Standard Library and Pip
- `import modulename as alias`
    - `alias.function()`
- `from modulename import function as alias, function as alias` - Alias is optional at this point
- Package: `my_modules`
    - file: `__init__.py`

### Section 7: Playwright Basics
- Documentation: `https://playwright.dev/python/docs/intro`
- initial commands:
    - `pip install pytest-playwright`
    - `playwright install`
    - `playwright codegen [web]`
- Test case is not a test case if there are no assertions
- AAA - Assess, Act, Assert
- Given/When/Then
- Slow_mo!
- Default timeout: page.set_default_timeout(3000)
- Per specific element, `page.wait_for_url("https://playwright.dev/docs/intro",timeout=####)`

### Section 8: Playwright Selectors
- first.click()
- Multime results`page.locator(":nth-match(:text('Shop'),1)")`
    - Index starts with 1, not 0
- Chaining selectors `css=article >> css.bar`

### Section 9: Assertions
- Python way of asserting: assert
- Playwright way: `expect(page.locator("text=Something")).something()`
- [Test Assertions](https://playwright.dev/python/docs/test-assertions)

### Section 10: Waits
- `page.wait_for_selector()`
- `page.wait_for_load_state()`
- `time.sleep(2)` (not recommended)
- While loop. 
```python
while login_issue:
    if not page.is_visible(selector):
        page.click(selector) # do something
    else
        login_issue = False
```

### Section 11: POM and Project Structure
- [POM](https://playwright.dev/python/docs/pom)
- Try using fixtures instead of Helpers

### Section 12: Pytest Framework Basics
- `pip install pytest-playwright`
- Naming convention:
    - packages/folder : "test*"; Example: "tests_ui_layout"
    - python files: "test*"; Example: "test_home_page_layout"
    - python functions/modules: "test*" Example: "test_about_us_section_verbiage"
    - python classes: "Test*" Example "TestHomePage"
- run `pytest`
- Markers:
    - Multiple markers can be used per test
    - Skip: `@pytest.mark.skip(reason="")` before the test function
        - import pytest
        - run `pytest -v`
    - xfail: `@pytest.mark.xfail(reason="")` before the test function
        - import pytest
        - run `pytest -v`
    - Custom: `@pytest.mark.smoke(reason="")` before the test function
        - Import pytest
        - Run `pytest -v`
        - Add pytest.ini root and add:
            [pytest]
            markers = 
                smoke: description
                regression: description
                integration: description

        - Samples:
            - `pytest -m marker`
            - `pytest -m "not smoke"`
            - `pytest -m "not smoke or integration"`
            - `pytest -m "not smoke" -v`
            - `@pytest.mark.integration`
            - `@pytest.mark.regression`
            - `@pytest.mark.integration`
- pytest CLI commands
    - Stop at first failure: `pytest -x`
    - Allow max failures before stopping: `pytest --maxfail=2`
    - Run single test: `pytest -k test_func_name`
    - Run a single file: `pytest test_file.py`
    - Re-run last failed tests only: `pytest --lf`
    - Re-run all tests, starting with last failed: `pytest --ff`
    - You can combine CLI options together: `pytest --ff -x -v`
    - Reporting with pytest-reporter-html1: `pytest --template=html1/index.html --report=report.html`

### Section 13: Reporting and Parallel Execution via CLI
- `pip install pytest-reporter-html1`
- `pip install pytest-xdist`
- `pytest -n auto` or `pytest -n 3`
- `pytest --maxfail=2 -m regression --template=html1/index.html --report=regression.html -n4`

### Section 14: Pytest - Playwright fictures and CLI commands
- Fixutes = Context for test
- `conftest.py`
- use yield instead of return
- [Fixtures](https://playwright.dev/python/docs/test-runners#fixtures)
- Playwright's built in fixture: 'page'
- CLI Commands
    - [test-runners](https://playwright.dev/python/docs/test-runners)
    - --headed: Run tests in headed mode (default: headless).
    - --browser: Run tests in a different browser chromium, firefox, or webkit. It can be specified multiple times (default: all browsers).
    - --browser-channel Browser channel to be used.
    - --slowmo Run tests with slow mo.
    - --device Device to be emulated.
    - --video Whether to record video for each test. on, off, or retain-on-failure (default: off).
    - --screenshot Whether to automatically capture a screenshot after each test. on, off, or only-on-failure (default: off).
    - --base-url Specify a base url
    - --output=nameofthefolder

- [Scopes](https://playwright.dev/python/docs/test-runners)
- Example, for login use:
    ```python
    @pytest.fixture(scope="session")
    def set_up(browser):
        context = browser.new_content()
        page = context.new_page()
        page.goto("link")
        ...
        yield page
        page.close()
    ```


### Section 15: Data Driven Testing
- marker: `@pytest.mark.parametrize`
- Sample: 
    ```python
    @pytest.mark.parametrize("name, email, message",[("Test Name 1", "test1@testingcorp.com","This is test sample 1"),
                                                    ("Test Name 2", "test2@testingcorp.com", "This is test sample 2"),
                                                    pytest.param("Test Name 3", "test3@testingcorp.com", "This is test sample 3", marks=pytest.mark.xfail)] )
    def test_contact_page_form(set_up_contact_page_fill, name, email, message) -> None:
        ...
    ```
