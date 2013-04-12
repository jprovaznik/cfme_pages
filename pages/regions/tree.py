'''
Created on Mar 7, 2013

@author: bcrochet
'''

# -*- coding: utf-8 -*-

from pages.page import Page
from selenium.webdriver.common.by import By

class Tree(Page):
    '''
    classdocs
    '''

    _main_tree_item_locator = (By.CSS_SELECTOR, "table > tbody > tr > td > table > tbody")
    _root_item_locator = (By.XPATH, "tr")
    _sub_item_locator = (By.XPATH, "following-sibling::*")
    
    def __init__(self,setup,root_element,parent = None, item_class = Tree):
        Page.__init__(self, setup)
        self._root_element = root_element
        self._parent = parent
        self.item_class = item_class
        
    @property
    def root(self):
        return self._root_element.find_element(*self._main_tree_item_locator).find_element(*self._root_item_locator)
        
    @property
    def children(self):
        return [self._item_class(self.testsetup, web_element, self, self._item_class)
                for web_element in self.root.find_elements(*self._sub_item_locator)]
    
    @property
    def name(self):
        return self.root.text.encode('utf-8')
        
    @property
    def twisty(self):
        from pages.regions.twisty import Twisty
        return Twisty(self.testsetup, self.root)
    
    @property
    def parent(self):
        return self._parent
        
    def is_displayed(self):
        return self._root_element.is_displayed()
   
    #def find_child_by_name(self, name):
    #    for child in children:
    #      return child if child.
