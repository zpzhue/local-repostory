# coding = utf-8

from selenium import webdriver
import time
connect_baidu=webdriver.Chrome()

connect_baidu.get('https://www.baidu.com')

connect_baidu.find_element_by_xpath('//*[@id="u1"]/a[8]').click()
connect_baidu.find_element_by_class_name('setpref').click()

time.sleep(2)
connect_baidu.find_element_by_id('nr').find_element_by_xpath('//option[@value="20"]').click()


connect_baidu.find_element_by_css_selector('a[class=\"prefpanelgo\"]').click()
connect_baidu.switch_to_alert().accept()

connect_baidu.find_element_by_id('kw').send_keys('python')
connect_baidu.find_element_by_id('su').click()
