from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui

options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
# options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1 })
options.add_argument("--start-maximized")

driver = webdriver.Chrome('D:\\chromedriver.exe', options=options)
time.sleep(1)

driver.get('http://facebook.com')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="email"]').send_keys('USERNAME')
# time.sleep(1)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('PASSWORD')
time.sleep(1)
login = driver.find_element_by_xpath('//*[@id="u_0_d"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*["a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7"]').click()
c=("hi")
pyautogui.typewrite("c")
# driver.find_element_by_class_name('a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7').send_keys("hi")

# ActionChains(g).click()
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[2]/div/div/div/div/label/input').click()
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[2]/div[2]/div/div/div/div/label/input').send_keys('wardha')
driver.find_element_by_xpath('//*[@id="jsc_c_9y"]/div/a/div/div[1]/div/div').click()
driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div[3]/a/div/div[2]/div').click()
# driver.execute_script("window.scrollTo()")



time.sleep(1)
driver.get("https://www.facebook.com/photo/?fbid=2830869873856930&set=a.1375661799377752")
driver.find_element_by_class_name('_1mf _1mj"]').click()
c=("hi")
driver.find_element_by_class_name('_1mf _1mj').click()
pyautogui.typewrite(c)
# pyautogui.press('enter')
time.sleep(5)
# driver.find_element_by_xpath('//*[@id="mount_0_0"]').send_keys("thi is an automated text")
# time.sleep(5)

