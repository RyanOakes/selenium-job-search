import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


job_links = {
    1: 'http://indeed.com',
    2: 'http://monster.com',
    3: 'http://simplyhired.com',
}

class JobQuery():

    def __init__(self, website, description, zipcode):
        self.website = website
        self.description = description
        self.zipcode = zipcode

    def indeed_search(self):
        browser = webdriver.Chrome()
        browser.get(job_links[self.website])
        jobs = browser.find_element_by_id('what')
        jobs.send_keys(self.description)
        location = browser.find_element_by_id('where').clear()
        location = browser.find_element_by_id('where')
        location.send_keys(self.zipcode)
        location.send_keys(Keys.ENTER)

    def monster_search(self):
        browser = webdriver.Chrome()
        browser.get(job_links[self.website])
        jobs = browser.find_element_by_id('q1')
        jobs.send_keys(self.description)
        location = browser.find_element_by_id('where1')
        location.send_keys(self.zipcode)
        location.send_keys(Keys.ENTER)

    def simplyhired_search(self):
        browser = webdriver.Chrome()
        browser.get(job_links[self.website])
        jobs = browser.find_element_by_name('q')
        jobs.send_keys(self.description)
        location = browser.find_element_by_name('l')
        location.send_keys(self.zipcode)
        location.send_keys(Keys.ENTER)


    def create_browser_and_search(self):
        if self.website == 1:
            self.indeed_search()
        elif self.website == 2:
            self.monster_search()
        else:
            self.simplyhired_search()
