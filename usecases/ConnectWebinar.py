# -*- coding: utf-8 -*-
from BasicCase import BasicCase
from pages.SignPage import SignPage

import time

class ConnectWebinar(BasicCase):
    
    def setUp(self):
        super(ConnectWebinar, self).setUp()
        self.sign_page = SignPage(self.driver)
        self.sign_page.open('http://webinar.bmstu.ru/b/address_of_webinar')
        
    def test_perform(self):
        name = 'Тестовое имя'
        name = name.decode('utf-8', errors='ignore')
        self.sign_page.input_name(name)
        self.sign_page.click_join_btn()
        self.sign_page.click_audio_btn()
        
    