# -*- coding: utf-8 -*-
import os
import random
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

import config


class BasicCase(object):

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        self.driver = webdriver.Chrome(config.DRIVER, chrome_options=chrome_options)

    def add_random_number(self, string):
        return string + str(random.randrange(1, 1000000))
