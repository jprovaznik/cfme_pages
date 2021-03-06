#!/usr/bin/env python

# -*- coding: utf-8 -*-

import pytest
import time
from unittestzero import Assert

@pytest.mark.nondestructive
class TestInfrastructureTab:
    def test_infrastructure_tab(self, mozwebqa, home_page_logged_in):
        home_pg = home_page_logged_in
        Assert.true(home_pg.is_logged_in, "Could not determine if logged in")
        infra_pg = home_pg.header.site_navigation_menu("Infrastructure").click()
        Assert.true(infra_pg.is_the_current_page)
        pxe_pg = infra_pg.header.site_navigation_menu("Infrastructure").sub_navigation_menu("PXE").click()
        Assert.true(pxe_pg.is_the_current_page)
