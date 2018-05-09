from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
from django.contrib.auth.models import User
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope='module')
def browser(request):
    """Provide a selenium webdriver instance."""

    # options.add_argument('headless')
    options = Options()
    options.add_argument('-headless')
    browser_ = webdriver.Firefox(firefox_options=options)
    yield browser_    # TearDown
    browser_.quit()


@pytest.mark.django_db
def test_login(live_server, browser):

    browser.get("http://localhost:8000")
    User.objects.create(username='admin', password='adminadmin')
    browser.find_element_by_id('id_username').send_keys('admin')
    browser.find_element_by_id('id_password').send_keys('adminadmin')
    browser.find_element_by_id('btnLogin').click()

    browser.find_element_by_id('newProject').click()
    element = browser.find_element_by_id('id_user')
    all_options = element.find_elements_by_tag_name("option")
    for option in all_options:
        option.click()
    browser.find_element_by_id(
        'id_project_name').send_keys('this is a project name')
    browser.find_element_by_id(
        'id_description').send_keys('this is a description')
    browser.find_element_by_id('btn-save').click()

    browser.find_element_by_id('btnLogout').click()
