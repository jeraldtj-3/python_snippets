
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import wget
import time

# driver setup 
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.facebook.com")

# facebook authentication 
def authentication(user,passwd):
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
    username.clear()
    username.send_keys(str(user))
    password.clear()
    password.send_keys(str(passwd))
    button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

authentication(user = "",passwd="" )

# friends list page 
driver.get("https://www.facebook.com/friends/list/")
friends_element = driver.find_elements(By.CSS_SELECTOR,'a[class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 mg4g778l pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb btwxx1t3 abiwlrkh p8dawk7l lzcic4wl ue3kfks5 pw54ja7n uo3d90p7 l82x9zwi a8c37x1j"]')

profile_urls = [i.get_attribute('href') for i in friends_element]

def filter_profile(profile_url):
    '''removing the profile urls with id '''
    if profile_url.split('/')[3].startswith('profile'):
        return False
    else:
        return True

profile_urls = [i for i in profile_urls if filter_profile(i)]

from tqdm import tqdm 
work_and_education = []
for profile_url in tqdm(profile_urls):
    driver.get(profile_url)
    about_url = profile_url+'/about/'
    driver.get(about_url)
    work_and_education_link = profile_url+'/about_work_and_education/'
    driver.get(work_and_education_link)
    
    try:
       # work and education details 
        work_education_element = driver.find_elements(By.CSS_SELECTOR,'div[class="dati1w0a tu1s4ah4 f7vcsfb0 discj3wi"]')
        work_education_info = [i.get_attribute('innerText') for i in work_education_element] 
        work_and_education.append(work_education_info[0])
    except: 
        work_and_education.append('nan')

import pandas as pd 
df = pd.DataFrame({
    "profile_url":profile_urls,
    "work_education":work_and_education
    })
