# -*- coding: utf-8 -*-
#--------------------------------------------------------------
#!/usr/bin/env python
# Author:
#   Quinn Song <quinn4dev@gmail.com>
# Credit to: www.way2automation.com
# web_auto.py: python's unittest framework
# --------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest, time

class PythonDemoTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.way2automation.com"
        self.accept_alert = True
        self.verification_errors = []
    def openPage(self):
        driver = self.driver
        driver.get(self.base_url + '/demo.html')
        try: self.assertEqual(driver.title, u"Welcome")
        except AssertionError as e: self.verification_errors.append(str(e))
    def test_open_page(self):
        """ Open Base URL:
        --------------------------------------------------
        Open up the url -> Assert the page title -> Quit!
        --------------------------------------------------"""        
        self.openPage()
    def test_alert_present(self):
        """ Work with Alert:
        ----------------------------------------------------------------------------
        1. Open up the url -> Assert the page title
        2. WebDriverWait (timeout: 10s) until Alert link clickable;
        3. Sleep 5s for new tab window;
        4. Switch to new window;
        5. Assert new window title;
        6. Sleep 5s for new alert pop up;
        7. Assert alert pop up;
        8. Assert alert text "REGISTRATION FORM"
        9. Fill out Registration Form:
            [Note] tricky for last three elements (i.e. username, password, submit).
            It's so easy to land on invisable elements at bottom layer; Using a
            different xpath can solve the issue.
            -----------------------------------------------------------------------""" 
        self.openPage()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, ur"//section/div[2]/div[2]/div[6]/ul/li/a/figure"))
            )
            if self.is_element_present(By.XPATH, ur"//section/div[2]/div[2]/div[6]/ul/li/a/figure"):
                self.driver.find_element(By.XPATH, ur"//section/div[2]/div[2]/div[6]/ul/li/a/figure").click()

            try:  self.assertTrue(EC.new_window_is_opened)
            except AssertionError as e: self.verification_errors.append(str(e))
            
            time.sleep(5) # wait for new tab available           
         
            self.driver.switch_to_window(self.driver.window_handles[-1])
            
            try: self.assertEqual(self.driver.title, u"Welcome to the Test Site")
            except AssertionError as e: self.verification_errors.append(str(e))
            time.sleep(5) # wait for new alert popup
            
            try: self.assertTrue( EC.alert_is_present)
            except AssertionError as e: self.verification_errors.append(str(e))
            
            alert = self.driver.switch_to_alert()
            
            try: self.assertEqual(self.driver.find_element_by_xpath("//form[@class='ajaxsubmit']/h3").text, "REGISTRATION FORM")
            except AssertionError as e: self.verification_errors.append(str(e))
            
            # Fill out registration form
            self.driver.find_element_by_xpath("//input[@name='name']").send_keys("John You")
            self.driver.find_element_by_xpath("//input[@name='phone']").send_keys("212-2121")
            self.driver.find_element_by_xpath("//input[@name='email']").send_keys("john.you@email.com")
            
            select = Select(self.driver.find_element_by_name("country"))            
            select.select_by_value("Canada")
            #Or: select.select_by_visible_text("Canada")
            
            self.driver.find_element_by_xpath("//input[@name='city']").send_keys("Calgary")
            # The following 3 elements are tricky; easy to get  "ElementNotVisibleException"
            self.driver.find_element_by_xpath("//form/fieldset[6]/input").send_keys("quinn")
            self.driver.find_element_by_xpath("//form/fieldset[7]/input").send_keys("song")
            self.driver.find_element_by_xpath("(//form/div/div[2]/input)[2]").click()
            
        except Exception as e:
            self.verification_errors.append(str(e))
        
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
            return True
        except NoSuchElementException as e:
            return False            
        
    def tearDown(self):
        self.driver.quit()
        self.assertListEqual([], self.verification_errors)
        
if __name__ == '__main__':
    #unittest.main()
     suite = unittest.TestLoader().loadTestsFromTestCase(PythonDemoTest)
     unittest.TextTestRunner(verbosity=2).run(suite)
        