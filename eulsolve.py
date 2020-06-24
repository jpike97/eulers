from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")

number = input("Which Euler do you want to solve? ")

if int(number) < 12:

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://euler.stephan-brumme.com/" + number)
    driver.find_element_by_id('live_button').click()

    time.sleep(1)

    result = driver.find_element_by_id('live_output').text
    print(result)

else:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.mathblog.dk/project-euler-" + number)

    time.sleep(1)

    result = driver.find_element_by_xpath("//code[@class='plain plain']").text 
    print (result)



driver.close()