# coding=UTF-8
import sys
import pickle
import logging
import requests
import json
import argparse
import html5lib

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep

class Crawler():
    def __init__(self):
        self.URL = 'https://www.instagram.com/'
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-u','--user', nargs='?', help='instagram user')
        parser.add_argument('-p','--pw', nargs='?', help='instagram passwd')
        args = vars(parser.parse_args())
        if not args['user'] or not args['pw']:
            print('please type instagram username and password')
            sys.exit()
        self.user = args['user']
        self.passwd = args['pw']

    def awake_driver(self):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        # options.add_argument('--headless')
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(self.URL)

    def run(self):
        self.awake_driver()
        sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(self.user)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(self.passwd)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
        sleep(3)
        cookies = self.driver.get_cookies()
        with open('res.json','w',encoding='utf-8') as f:
            json.dump(cookies,f,indent=2,sort_keys=True,ensure_ascii=False)
        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    crawler = Crawler()
    crawler.run()