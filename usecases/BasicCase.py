# -*- coding: utf-8 -*-
import os
import unittest
import random
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

import config


class BasicCase(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        self.driver = webdriver.Chrome(config.DRIVER, chrome_options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def add_random_number(self, string):
        return string + str(random.randrange(1, 1000000))
