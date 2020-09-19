from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import os

TASK_DIR = os.path.abspath(os.curdir)


class AutomationTask:
    def __init__(self, chrome_driver=None, firefox_driver=None):
        self.chrome_driver = chrome_driver or webdriver.Chrome(ChromeDriverManager().install())
        self.firefox_driver = firefox_driver or webdriver.Firefox(GeckoDriverManager().install())

    # 1 and 2
    def automation_script_1(self):
        self.chrome_driver.get("http://www.walla.co.il")
        website_title = "וואלה! NEWS"
        self.chrome_driver.refresh()
        sleep(5)
        title = self.chrome_driver.find_element_by_css_selector("div.mobile-vertical-name a").get_attribute("title")
        assert title == website_title
        self.chrome_driver.close()
        self.firefox_driver.get("http://www.walla.co.il")

    # 3 - YES

    # 4 AND 6
    def automation_script_2(self):
        self.chrome_driver.get("https://translate.google.com/")
        self.chrome_driver.find_element_by_css_selector("#input-wrap textarea").send_keys("טסט")
        translation_text_field1 = self.chrome_driver.find_element_by_id("source")
        translation_text_field2 = self.chrome_driver.find_element_by_css_selector("#input-wrap textarea")
        translation_text_field3 = self.chrome_driver.find_element_by_css_selector("div.source-wrap #source")

    # 5
    def automation_script_3(self):
        self.chrome_driver.get("https://https://www.youtube.com/")
        self.chrome_driver.find_element_by_css_selector("#search-input input").send_keys("chill music")
        search_button = self.chrome_driver.find_element_by_css_selector("#search-form button")
        search_button.click()

    # 7
    def automation_script_4(self):
        self.chrome_driver.get("https://www.facebook.com/")
        username = self.chrome_driver.find_element_by_css_selector("#email")
        password = self.chrome_driver.find_element_by_css_selector("#password")
        username.send_keys("test@test.com")
        password.send_keys("test123456")
        login_button = self.chrome_driver.find_element_by_name("login")
        login_button.click()

    # 8
    def automation_script_5(self):
        self.chrome_driver.get("https://https://www.youtube.com/")
        self.chrome_driver.delete_all_cookies()
        cookies_list = self.chrome_driver.get_cookies()
        assert not cookies_list

    # 9
    def automation_script_6(self):
        self.chrome_driver.get("http://www.walla.co.il")
        search_area = self.chrome_driver.find_element_by_css_selector("input.header-search-input")
        search_area.send_keys("test")
        search_area.send_keys(Keys.ENTER)

    # 10
    def automation_script_7(self):
        chrome_options = Options()
        chrome_driver_filename = '/chromedriver'
        chrome_driver_path = TASK_DIR + chrome_driver_filename
        webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

    def close_browsers(self):
        self.chrome_driver.close()
        self.chrome_driver.quit()
        self.firefox_driver.close()
        self.firefox_driver.quit()


def main():
    automation_task = AutomationTask()
    automation_task.automation_script_1()
    automation_task.automation_script_2()
    automation_task.automation_script_3()
    automation_task.automation_script_4()
    automation_task.automation_script_5()
    automation_task.automation_script_6()
    automation_task.automation_script_7()
    automation_task.close_browsers()


if __name__ == "__main__":
    main()
