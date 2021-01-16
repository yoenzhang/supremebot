from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import requests

def set_viewport_size(driver, width, height):
    window_size = driver.execute_script("""
        return [window.outerWidth - window.innerWidth + arguments[0],
          window.outerHeight - window.innerHeight + arguments[1]];
        """, width, height)
    driver.set_window_size(*window_size)

cart = open("cart.txt", 'r')
settings = open('setting.txt')
PATH = ('/Users/yoon/Downloads/chromedriver')
driver = webdriver.Chrome(PATH)
driver.set_page_load_timeout(30)
set_lines = settings.readlines()

# set the viewport size to 800 x 600
set_viewport_size(driver, 800, 600)

# display the viewport size
#print(driver.execute_script("return [window.innerWidth, window.innerHeight];"))

for line in cart:
    try:
        driver.get(line)
        search = driver.find_element_by_id('add-remove-buttons')
        time.sleep(0.25)
        button = search.find_element_by_class_name('button').click()
        time.sleep(0.5)
        driver.find_element_by_link_text("checkout now").click()
        driver.find_element_by_id('order_billing_name').send_keys(set_lines[0])
        driver.find_element_by_id('order_email').send_keys(set_lines[1])
        driver.find_element_by_id('order_tel').send_keys(set_lines[2])
        driver.find_element_by_id('bo').send_keys(set_lines[3])
        driver.find_element_by_id('oba3').send_keys(set_lines[4])
        driver.find_element_by_id('order_billing_zip').send_keys(set_lines[5])
        driver.find_element_by_id('order_billing_city').send_keys(set_lines[6])
        Select(driver.find_element_by_id('order_billing_state')).select_by_value(set_lines[7][:-1])
        Select(driver.find_element_by_id('order_billing_country')).select_by_value(set_lines[8][:-1])
        driver.find_element_by_id('rnsnckrn').send_keys(set_lines[9])
        Select(driver.find_element_by_id('credit_card_month')).select_by_value(set_lines[10][0:2])
        Select(driver.find_element_by_id('credit_card_year')).select_by_value(set_lines[10][3:-1])
        driver.find_element_by_id('orcer').send_keys(set_lines[11])
        box = driver.find_element_by_id('order_terms')
        driver.execute_script("arguments[0].click();", box)
        checkout = driver.find_element_by_id('pay')
        checkout.find_element_by_class_name('button').click()

    finally:
        time.sleep(200)
        driver.quit()
