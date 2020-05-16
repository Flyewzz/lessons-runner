# -*- coding: utf-8 -*-
import os
import random
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import config
import sys


class BasicCase(object):

    def __init__(self, no_sendbox, headless, executor, virtual_display):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru,ru_RU'})
        if headless:
            options.add_argument('headless')
            if no_sendbox:
                options.add_argument("-–no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                if virtual_display:
                    from pyvirtualdisplay import Display
                    display = Display(visible=0, size=(800, 600))
                    display.start()
                if not executor:
                    # Default value of executor
                    executor = 'http://localhost:4444/wd/hub'
                    
                self.driver = webdriver.Remote(
                    command_executor=executor,
                    desired_capabilities=DesiredCapabilities.CHROME,
                    options=options,
                )
                return
        self.driver = webdriver.Chrome(config.DRIVER, chrome_options=options)
