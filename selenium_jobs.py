import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

job_list = [x for x in range(4)]
job_sites = {
    1: 'Indeed',
    2: 'Monster',
    3: 'SimplyHired',
}


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def restart():
    verdict = input("\nAny luck? Would you like to initiate another job search?[y/N] \n")
    if verdict.lower() == 'y':
        return True


def user_selects_job_website():
    job_website = input("""\nFirst, please choose one of the following sites:\n
(1) Indeed
(2) Monster
(3) SimplyHired
    \nWhich site would you like to search? """)
    if int(job_website) and int(job_website) in job_list:
        pass
    else:
        clear()
        print("Please provide a number that corresponds with a particular website!")
        user_selects_job_website()
    return int(job_website)


def user_selects_job_search():
    job_description = input("\nWhat kind of job are you looking for? ")
    job_zipcode = input("\nWhat zip code would you like to search in? ")
    clear()
    print("""Gotcha. Let's see if we can find any {} positions in the {} area.""".format(job_description, job_zipcode))
    return job_description, job_zipcode


def load_job_website(job_website, job_description, job_zipcode):
    """Creates browser object and loads the user's search parameters
    MUST REFACTOR, way too busy."""

    if job_website == 1:
        browser = webdriver.Chrome()
        browser.get('http://indeed.com')
        jobs = browser.find_element_by_id('what')
        jobs.send_keys(job_description)
        location = browser.find_element_by_id('where').clear()
        location = browser.find_element_by_id('where')
        location.send_keys(job_zipcode)
        location.send_keys(Keys.ENTER)

    if job_website == 2:
        browser = webdriver.Chrome()
        browser.get('http://monster.com')
        jobs = browser.find_element_by_id('q1')
        jobs.send_keys(job_description)
        location = browser.find_element_by_id('where1')
        location.send_keys(job_zipcode)
        location.send_keys(Keys.ENTER)

    if job_website == 3:
        browser = webdriver.Chrome()
        browser.get('http://simplyhired.com')
        jobs = browser.find_element_by_name('q')
        jobs.send_keys(job_description)
        location = browser.find_element_by_name('l')
        location.send_keys(job_zipcode)
        location.send_keys(Keys.ENTER)


def main():

    clear()
    print("Welcome non-contributing zero! Let's get you employed.")

    job_website = user_selects_job_website()

    job_description, job_zipcode = user_selects_job_search()

    browser = load_job_website(job_website, job_description, job_zipcode)

    if restart():
        main()

    browser.quit()

    clear()


if __name__ == '__main__':
    main()
