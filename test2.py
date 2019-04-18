#!python3
#!commandlinemail.py

#コマンドラインからメールアドレスの入力、及びにテキストの入力

import requests, os , bs4
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://login.yahoo.com/?display=login&.intl=us&.lang=en-US&.src=fpctx&done=https%3A%2F%2Fwww.yahoo.com%2F&prefill=0&chllngnm=base')


#TODO:LOGIN TO yahoomail
#signin to yahoomail
signin_elem = browser.find_element_by_id('login-username')
signin_real = input('your email address: ')
signin_elem.send_keys(signin_real)

next_elem = browser.find_element_by_id('login-signin')
next_elem.click()

time.sleep(3)

#type a password
passwd_elem = browser.find_element_by_id('login-passwd')
passwd_real = input('your password: ')
passwd_elem.send_keys(passwd_real)

next2_elem = browser.find_element_by_id('login-signin')
next2_elem.click()

wait = WebDriverWait(browser, 10)
waiting_elem = wait.until(expected_conditions.element_to_be_clickable)


#go to mail page

tap_mailbutton = browser.find_element_by_id('uh-mail-link')
tap_mailbutton.click()

compose_button = browser.find_element_by_xpath("//a[@data-test-id='compose-button']")
compose_button.click()

#TODO:designate an email address
address_to = browser.find_element_by_id('message-to-field')
address_real = input('send TO : ')
address_to.send_keys(address_real)

#TODO:make content
#write something in Subject
subject_elem = browser.find_element_by_xpath("//input[@data-test-id='compose-subject']")
subject_real = input('subject: ')
subject_elem.send_keys(subject_real)
time.sleep(2)

#wrtie contents
contents_elem = browser.find_element_by_xpath("//div[@data-test-id='rte']")
contents_real = input('contents: ')
contents_elem.send_keys(contents_real)
time.sleep(2)
#TODO:send an email
send_elem = browser.find_element_by_xpath("//button[@data-test-id='compose-send-button']")
send_elem.click()
time.sleep(2)

browser.quit()


print('I am Done....')
