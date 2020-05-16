# -*- coding: utf-8 -*-
from BasicCase import BasicCase
from pages.SignPage import SignPage

import time
import sys

import selenium

reload(sys)
sys.setdefaultencoding('utf8')

class ConnectWebinar(BasicCase):
        
    def __init__(self, no_sendbox, headless, name, url, wait_time, 
                 presence_time, executor, key, virtual_display):
        super(ConnectWebinar, self).__init__(no_sendbox, headless, 
                                             executor, virtual_display)
        self.name = name
        self.url = url
        self.wait_time = wait_time
        self.presence_time = presence_time
        self.key = key
        self.sign_page = SignPage(self.driver)
        try:
            self.sign_page.open(self.url)
        except selenium.common.exceptions.TimeoutException:
            print('Timeout to open this url')
            self.driver.quit()
        
    def perform(self):
        try:
            if self.key:
                self.sign_page.input_key(self.key)
                self.sign_page.click_enter_btn(self.wait_time)
            self.sign_page.input_name(self.name)
            self.sign_page.click_join_btn(self.wait_time)
            self.sign_page.click_audio_btn(self.wait_time)
            time.sleep(self.presence_time)
        except selenium.common.exceptions.NoSuchElementException:
            print('No such element found')
        except selenium.common.exceptions.TimeoutException:
            print('Timeout to open this url')
        finally:
            self.driver.quit()
        
        
    