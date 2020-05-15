from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from BasicPage import BasicPage

import time

from selenium.webdriver import ActionChains

import sys


class SignPage(BasicPage):
    
    sign_name_input_field = 'input.join-form:not(#room_access_code)'
    sign_key_input_field = 'input.join-form#room_access_code'
    
    enter_btn = 'input.join-form[name="commit"]'
    join_btn = 'button.join-form'
    
    micro_btn = 'div[role="dialog"] > div button:first-of-type'
    audio_btn = 'div[role="dialog"] > div button:last-of-type'
    
    def open(self, url):
        self.driver.get(url)
        
    def input_name(self, name):
        elem = self.wait_render(self.sign_name_input_field)
        elem.clear()
        elem.send_keys(name)
        
    def input_key(self, key):
        elem = self.wait_render(self.sign_key_input_field)
        elem.clear()
        elem.send_keys(key)
        
    def click_enter_btn(self, wait_time=10):
        elem = self.wait_render(self.enter_btn, wait_time)
        elem.click()
    
    def click_join_btn(self, wait_time=10):
        elem = self.wait_render(self.join_btn, wait_time)
        elem.click()
        
    # Will require a permission to use your microphone (required manual confirmation)
    def click_micro_btn(self, wait_time=10):
        elem = self.wait_render(self.micro_btn, wait_time)
        elem.click()
        
    def click_audio_btn(self, wait_time=10):
        elem = self.wait_render(self.audio_btn, wait_time)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

        