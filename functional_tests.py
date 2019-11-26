from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_create_an_account(self):  
        # Michiel has heard about a cool new website to check out match statistics for his football team.
        # He goes to checkout the homepage.
        self.browser.get('http://localhost:8000')

        # He realizes he needs to create an account first, for he is immediately redirected to a login page.
        # self.assertIn('Login', self.browser.title)
        # self.assertIn('login', self.browser.current_url)

        # He goes to the registration page.
        # self.assertIn('Registration', self.browser.title)

        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
