from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os
from Config.Config import *
DEFAULT_SECONDS = 10

class BasePage(object):

    """页面对象基础类"""

    def __init__(self, driver):
        
        self.driver = driver
        self.C = Config()
        self.base_url = self.C.host
        self.driver.implicitly_wait(5)

    def kill_process(self, pid):

        pid_count = os.system("tasklist /M %s*" %pid)
        print(pid_count)
        if pid_count > 0:
            return_code = os.system("taskkill /F /iM %s.exe" %pid)
            if return_code == 0:
                print('成功结束Firefox浏览器进程！')
            else:
                print('结束Firefox浏览器进程失败！')

    def _open(self, url):
        '''
        open the two level path of the bbs
        Usage:
            driver._open(self.base_url+"/index.html")
        '''
        url = self.base_url + url
        self.driver.maximize_window()
        self.driver.get(url)

    def open(self):
        '''
        open bbs index . "https://www.baidu.com"
        Usage:
            driver.open()
        '''
        self._open(self.url)

    def by_text(self,the_text):
        locator = (By.LINK_TEXT,the_text)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_link_text(the_text)

    def by_id(self, the_id):
        locator = (By.ID, the_id)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_id(the_id)

    def by_name(self, the_name):
        locator = (By.NAME, the_name)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_name(the_name)

    def actionchains_click_element(self,element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def by_class(self, the_class):
        locator = (By.CLASS_NAME, the_class)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_class_name(the_class)

    def by_css(self, css):
        locator = (By.CSS_SELECTOR, css)
        WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element_by_css_selector(css)

    def js(self, js_text):
        return self.driver.execute_script(js_text)

    def screenshot_on_exception(self, locator):
        try:
            WebDriverWait(self.driver, DEFAULT_SECONDS).until(EC.visibility_of_element_located(locator))
        except TimeoutException as e:
            # print(self.gen_screenshot_path(locator))
            self.driver.get_screenshot_as_file(self.gen_screenshot_path(locator))
            msg = "Time out when locate element using %s: %s" %(locator[0], locator[-1])
            raise TimeoutException(msg)

    def gen_screenshot_path(self, locator):
        locator_str = "NoSuchElement_BY_%s_%s" %(locator[0], locator[-1])
        return "./screenshots/%s_%s.png" %(locator_str, time.time())

class Switch_Win_Page(BasePage):
    def switch_windows(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
