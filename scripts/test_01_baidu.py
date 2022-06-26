import sys, os
sys.path.append(os.getcwd())
import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By



class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get('https://www.baidu.com')
        cls.baidu_sub = cls.driver.current_window_handle

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(1)").click()
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
        self.assertIn('news.baidu.com', self.driver.current_url)
        self.driver.close()
        self.driver.switch_to.window(self.baidu_sub)
        time.sleep(1)

    def test_02(self):
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(2)").click()
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
        self.assertIn('www.hao123.com', self.driver.current_url)
        self.driver.close()
        self.driver.switch_to.window(self.baidu_sub)
        time.sleep(1)

    def test_03(self):
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(6)").click()
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
        self.assertIn('image.baidu.com', self.driver.current_url)
        self.driver.close()
        self.driver.switch_to.window(self.baidu_sub)
        time.sleep(1)

    def test_04(self):
        self.driver.find_element(By.CSS_SELECTOR, "#s-top-left > a:nth-child(4)").click()
        all_handles = self.driver.window_handles
        self.driver.switch_to.window(all_handles[-1])
        self.assertIn('tieba.baidu.com', self.driver.current_url)
        self.driver.close()
        self.driver.switch_to.window(self.baidu_sub)
        time.sleep(1)


if __name__ == '__main__':
    unittest.main()