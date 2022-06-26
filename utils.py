



def switch_to_handle(self, url):
    all_handles = self.driver.window_handles
    for i in all_handles:
        if i != self.baidu_sub:
            self.driver.switch_to.window(i)
    self.assertEqual(url, self.driver.current_url)
    self.driver.close()
    self.driver.switch_to.window(self.baidu_sub)