import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption ('--language', action = 'store', default = None, help = "Choose GUI language for tests")
    parser.addoption('--browser', action='store', default='chrome')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption ("language")
    if language is None: raise pytest.UsageError("test run should contain language for test")

    browser = request.config.getoption('--browser')
    driver_name = dict(
        chrome='chromedriver'
    )[browser]
    driver_path = path.join(drivers_dir, driver_name)
    if browser == 'firefox':
        driver = webdriver.Firefox(executable_path=driver_path,
                                   log_path=log_path,
                                   firefox_options=ff_opts)
    elif browser == 'chrome':
        driver = webdriver.Chrome(executable_path=driver_path,
                                  service_log_path=log_path,
                                  chrome_options=ch_opts)
    driver.delete_all_cookies()

    def driver_finalizer():
        driver.quit()

    request.addfinalizer(driver_finalizer)
    return driver

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    print("\nopen browser for test..")
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)

    yield browser
    print("\nquit browser..")
    browser.quit()
