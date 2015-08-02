# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import time

#Automatic sign in sinablog

def login(username,password):
    browser = webdriver.Firefox()
    browser.get("http://weibo.com/login.php")
    wait = ui.WebDriverWait(browser,10)

    user = browser.find_element_by_xpath("//div[@class='W_login_form']/div[@class = 'info_list']/div[@class = 'inp username']/input")
    user.send_keys(username, Keys.ARROW_DOWN)
 
    passwd = browser.find_element_by_xpath("//div[@class='W_login_form']/div[@class = 'info_list']/div[@class = 'inp password']/input")
    passwd.send_keys(password, Keys.ARROW_DOWN)
 	
    browser.find_element_by_xpath("//div[@class = 'info_list login_btn']/div[1]/a[@class = 'W_btn_g']/span").click()
    wait.until(lambda browser: browser.find_element_by_xpath("//div[@class = 'B_home B_discover']"))
    print "nihao"

 
 
def test():
    username = "XXXXXXXXXXX"
    passwd = "XXXXXXXXXXX"
    login(username, passwd)
 
if __name__ == "__main__":
    test()

