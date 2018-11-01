from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_startretrieve(self):
        # Person goes to online app.
        self.browser.get('http://localhost:8000/user_accounts/signup')
        
        
        # Person notices title and header mention something
        self.assertIn('', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('Sign up', header_text)
        
        # Person tries to signup
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Sign in please'
        )
        
        # Person successfully signs up and is brought to their homepage
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        
        # Person browses the different surveys available
        
        # Person tries to take a new survey
        
        # Person successfully takes a new survey and gets to see their results compared to other peoples
        
        # Person logs out successfully 
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
