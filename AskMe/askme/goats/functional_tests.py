from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_startretrieve(self):
        # Person goes to online app.
        browser.get('http://localhost:8000')
        
        self.asserIn('askme', self.browser.title)
        self.fail('Finish the test!')
        
        # Person notices title and header mention something
        
        # Person tries to signup
        
        # Person successfully signs up and is brought to their homepage
        
        # Person browses the different surveys available
        
        # Person tries to take a new survey
        
        # Person successfully takes a new survey and gets to see their results compared to other peoples
        
        # Person logs out successfully 

if __name__ == '__main__':
    unittest.main(warnings='ignore')
