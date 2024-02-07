from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import requests
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://twitter.com/i/bookmarks")

input("Sign in, fullscreen, and press enter:")

while(True):
    content = driver.find_elements(By.CLASS_NAME, 'css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu')
    content = content[0].find_elements(By.CLASS_NAME, 'css-175oi2r.r-9aw3ui.r-1s2bzr4')
    imgs = content[0].find_elements(By.TAG_NAME, 'a')
    link = [i for i in imgs if len(i.find_elements(By.TAG_NAME, 'img')) > 0]
    link[0].click()

    for i in range(len(link)):
        img = driver.find_elements(By.TAG_NAME, 'img')
        img_url = img[i].get_attribute('outerHTML')
        img_url = img_url.split('src=')[1].split(' class')[0].replace('"', '').replace('amp;','')
        req = requests.get(img_url)
        name = img_url.split('?')[0].split('/')[-1]
        form = img_url.split('format=')[-1].split('&')[0]
        f = open('temp/'+name+'.'+form, 'wb')
        f.write(req.content)
        f.close()
    
    if len(link) > 2:
        input("Large collection detected. Download manually then press enter.")
    button = driver.find_element(By.CLASS_NAME, 'css-175oi2r.r-1kbdv8c.r-18u37iz.r-1oszu61.r-3qxfft.r-s1qlax.r-2sztyj.r-1efd50x.r-5kkj8d.r-h3s6tt.r-1wtj0ep')
    buttons = button.find_elements(By.CLASS_NAME, 'css-175oi2r.r-1777fci.r-bt1l66.r-bztko3.r-lrvibr.r-1loqt21.r-1ny4l3l')
    buttons[3].click()
    driver.back()
    time.sleep(1)
    

