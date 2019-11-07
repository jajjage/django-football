from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):  
        # Michiel has heard about a cool new website to check out match statistics for his football team.
        # He goes to checkout the homepage.
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention 'Football'
        self.assertIn('Football', self.browser.title)
        # He realizes he needs to create an account first, for he is immediately taken to a login page.
        self.assertIn('login', self.browser.url)

        self.fail('Finish the test!')

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
