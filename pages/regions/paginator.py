# -*- coding: utf-8 -*-
from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class Paginator(Page):
    '''Add this region to your page with a property called paginator
    
    Example:
    @property
    def paginator(self):
        from pages.regions.paginator import Paginator
        return Paginator(self.testsetup)
        
    '''
    #Navigation
    _first_page_locator = (By.CSS_SELECTOR, "#paging_div * img[alt='First']")
    _prev_locator = (By.CSS_SELECTOR, "#paging_div * img[alt='Previous']")
    _next_locator = (By.CSS_SELECTOR, "#paging_div * img[alt='Next']")
    _last_page_locator = (By.CSS_SELECTOR, "#paging_div * img[alt='Last']")

    #Position
    _position_text_locator = (By.CSS_SELECTOR, '#paging_div > #pc_div_1 > table > tbody > tr > td > table > tbody > tr > td:last-child')
    
    def click_first_page(self):
        self.selenium.find_element(*self._first_page_locator).click()
        self._wait_for_results_refresh()

    def click_prev_page(self):
        self.selenium.find_element(*self._prev_locator).click()
        self._wait_for_results_refresh()

    @property
    def is_prev_page_disabled(self):
        return 'dimmed' in self.selenium.find_element(*self._prev_locator).get_attribute('class')

    @property
    def is_first_page_disabled(self):
        return 'dimmed' in self.selenium.find_element(*self._first_page_locator).get_attribute('class')

    def click_next_page(self):
        self.selenium.find_element(*self._next_locator).click()
        self._wait_for_results_refresh()

    @property
    def is_next_page_disabled(self):
        return 'dimmed' in self.selenium.find_element(*self._next_locator).get_attribute('class')

    def click_last_page(self):
        self.selenium.find_element(*self._last_page_locator).click()
        self._wait_for_results_refresh()

    @property
    def is_last_page_disabled(self):
        return 'dimmed' in self.selenium.find_element(*self._last_page_locator).get_attribute('class')
