import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from ddt import ddt, data, unpack
# @ddt
class TestCaseFoo():
    # @data(("DEL","Patna"))
    # @unpack
    Org="DEL"
    DPR="Patna"
    def test_DDT(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://www.makemytrip.com/")
        driver.maximize_window()
        org = driver.find_element(By.XPATH, "//input[@type='text']")
        org.click()
        dpr = driver.find_element(By.XPATH, "//input[@placeholder='From']")
        # dpr.send_keys("DEL")
        dpr.send_keys(self.Org)
        all = driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']")
        time.sleep(4)
        print(len(all))
        for a in all:
            if "New Delhi" == a.text:
                a.click()
                time.sleep(4)
                break
        attg = driver.find_element(By.XPATH, "//label[@for='toCity']")
        attg.click()

        TOO = driver.find_elements(By.XPATH, "//div[@id='react-autowhatever-1']")
        driver.save_screenshot("C:/Testing/save.png")
        print(len(TOO))
        for t in TOO:
            # if "Patna" == t.text:
            if self.DPR == t.text:
                t.click()

                time.sleep(4)
                break
        driver.find_element(By.XPATH, "//p[@data-cy='departureDate']").click()

obj=TestCaseFoo()
obj.test_DDT()