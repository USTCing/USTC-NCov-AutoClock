# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 20:53:29 2021

@author: Dun
"""
# =============================================================================
# USTC 健康打卡 自动打卡
# =============================================================================

from selenium import webdriver
import time

chrome = webdriver.Chrome()

wlt = 'http://wlt.ustc.edu.cn/'
chrome.get(wlt)

wlt_user = chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/p/table/tbody/tr[2]/td[2]/input')
wlt_pwd = chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/p/table/tbody/tr[3]/td[2]/input')
wlt_user.send_keys("jiadun")
wlt_pwd.send_keys("820615")
time.sleep(1)
wlt_login = chrome.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td/p/table/tbody/tr[5]/td/input[2]').click()

url = 'https://weixine.ustc.edu.cn/2020/login'
chrome.get(url)
login = chrome.find_element_by_xpath('//*[@id="user-login"]/div/div[3]/div[2]/a').click()

username = chrome.find_element_by_xpath('//*[@id="username"]')
password = chrome.find_element_by_xpath('//*[@id="password"]')

username.send_keys("BA19232012")
password.send_keys("Ustc0802..")

log_in = chrome.find_element_by_xpath('//*[@id="login"]').click()


time.sleep(2)
submit = chrome.find_element_by_xpath('//*[@id="report-submit-btn"]').click()
# # input("程序运行结束！")  # 保证程序运行完成后窗口不会立即关闭