# coding = utf-8
import os
import time
from selenium import webdriver

fp = webdriver.FirefoxProfile(os.path.expanduser('~/Library/Application Support/Firefox/Profiles/0hn8nym4.default/'))
fp.set_preference("javascript.enabled",False)
browser = webdriver.Firefox(firefox_profile=fp)
browser.get('https://www.google.com.tw/')
search_box = browser.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(3)
aTags =  browser.find_elements_by_xpath("//h3/a")
for aTag in aTags:
    print aTag.get_attribute("href")



browser.close()