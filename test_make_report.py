import pytest
from selenium import webdriver
import random
import time
login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_sign_up():
  #Data
    unique_var = random.randint(1,1000000)
    password = "12_12_1234"

    sign_up_email = "#id_registration-email"
    sign_up_password1 = "#id_registration-password1"
    sign_up_password2 = "#id_registration-password2"
    sign_up_submit = "registration_submit"

#Arrange
    browser = webdriver.Chrome()
    browser.get(login_page_link)
    #Act
    email = browser.find_element_by_css_selector(sign_up_email)
    email.send_keys("{}@example.com".format(unique_var))
    password1 = browser.find_element_by_css_selector(sign_up_password1)
    password1.send_keys(password)
    password2 = browser.find_element_by_css_selector(sign_up_password2)
    password2.send_keys(password)
    button_submit = browser.find_element_by_name(sign_up_submit)
    button_submit.click()

    time.sleep(1)

    #Assert
    welcome_text_elt = browser.find_element_by_css_selector(".alertinner.wicon")
    welcome_text = welcome_text_elt.text

    assert "Спасибо за регистрацию!" == welcome_text

