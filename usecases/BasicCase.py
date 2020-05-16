# -*- coding: utf-8 -*-
import os
import random
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import config


class BasicCase(object):

    def __init__(self, no_sendbox, headless):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        if headless:
            from pyvirtualdisplay import Display
            options.add_argument('headless')
            if no_sendbox:
                options.add_argument("-–no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                display = Display(visible=0, size=(800, 600))
                display.start()
        
        self.driver = webdriver.Remote(
            command_executor='http://docker.for.mac.localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options,
        )
