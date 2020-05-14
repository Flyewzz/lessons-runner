from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from BasicPage import BasicPage

import time

from selenium.webdriver import ActionChains

class SignPage(BasicPage):
    
    sign_name_input_field = 'input.join-form'
    join_btn = 'button.join-form'
    
    micro_btn = 'div[role="dialog"] > div button:first-of-type'
    audio_btn = 'div[role="dialog"] > div button:last-of-type'
    
    def open(self, url):
        self.driver.get(url)
        
    def input_name(self, name):
        elem = self.wait_render(self.sign_name_input_field)
        elem.clear()
        elem.send_keys(name)
        
    def click_join_btn(self):
        elem = self.wait_render(self.join_btn)
        elem.click()
        
    # Will require a permission to use your microphone (required manual confirmation)
    def click_micro_btn(self):
        elem = self.wait_render(self.micro_btn)
        elem.click()
        
    def click_audio_btn(self):
        elem = self.wait_render(self.audio_btn)
        ActionChains(self.driver).move_to_element(elem).click(elem).perform()

        