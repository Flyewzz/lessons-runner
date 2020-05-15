# -*- coding: utf-8 -*-
import os
import random
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote

import config


class BasicCase(object):

    def __init__(self, headless):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        if headless:
            options.add_argument('headless') 
        
        self.driver = webdriver.Chrome(config.DRIVER, chrome_options=options)
