import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test(self):
        driver = self.driver
        driver.get("http://localhost:8000")
        self.login()
        self.createProject()
        self.logout()

    def login(self):
        self.driver.find_element_by_id('id_username').send_keys('admin')
        self.driver.find_element_by_id('id_password').send_keys('adminadmin')
        self.driver.find_element_by_id('btn-login').click()

    def createProject(self):
        self.driver.find_element_by_id('newProject').click()
        element = self.driver.find_element_by_id('id_user')
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            option.click()
        self.driver.find_element_by_id(
            'id_project_name').send_keys('this is a project name')
        self.driver.find_element_by_id(
            'id_description').send_keys('this is a description')
        self.driver.find_element_by_id('btn-save').click()

    def logout(self):
        self.driver.find_element_by_id('btnLogout').click()

    def tearDown(self):
        self.driver.close()
