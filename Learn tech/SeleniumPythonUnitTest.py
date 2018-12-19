import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Demo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('D:\Programming Software\chromedriver')
    def test_login_in_demo(self):
        driver = self.driver
        driver.get("http://www.facebook.com")
        self.assertIn("Facebook", driver.title)            # Dose a in b ?
        username = driver.find_element_by_id("email")
        username.send_keys("thierrysong29@yahoo.com")
        password = driver.find_element_by_id("pass")
        password.send_keys("94s03b25y")
        loginbutton = driver.find_element_by_id("loginbutton")
        loginbutton.click()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()