'''
Created on Apr 11, 2013

@author: jprovazn
'''

# -*- coding: utf-8 -*-

from pages.page import Page
from selenium.webdriver.common.by import By
from pages.regions.tree import Tree

class CheckboxTree(Tree):
    '''
    classdocs
    '''

    def check(self):
        return self._root_element.is_displayed()

    @property
    def children(self):
        return [CheckboxTree(self.testsetup, web_element, self)
                for web_element in self.root.find_elements(*self._sub_item_locator)]
