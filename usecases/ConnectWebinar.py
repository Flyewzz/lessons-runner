# -*- coding: utf-8 -*-
from BasicCase import BasicCase
from pages.SignPage import SignPage

import time
import sys

reload(sys)
sys.setdefaultencoding('utf8')

class ConnectWebinar(BasicCase):
        
    def __init__(self, headless, name, url, wait_time, presence_time, key):
        super(ConnectWebinar, self).__init__(headless)
        self.name = name
        self.url = url
        self.wait_time = wait_time
        self.presence_time = presence_time
        self.key = key
        self.sign_page = SignPage(self.driver)
        self.sign_page.open(self.url)
        
    def perform(self):
        if self.key:
            self.sign_page.input_key(self.key)
            self.sign_page.click_enter_btn(self.wait_time)
        self.sign_page.input_name(self.name)
        self.sign_page.click_join_btn(self.wait_time)
        self.sign_page.click_audio_btn(self.wait_time)
        time.sleep(self.presence_time)
        self.driver.close()
        
        
    