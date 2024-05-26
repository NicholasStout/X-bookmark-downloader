from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


import requests
import time

POST_NAME='css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-kzbkwu'
POST_IMAGE_NAME='css-175oi2r.r-1pi2tsx.r-1ny4l3l.r-1loqt21'

service = webdriver.FirefoxService(executable_path='/home/knil/Projects/WebDrivers/geckodriver')
options = webdriver.FirefoxOptions()
options.add_argument('--start-maximized');
options.add_argument('--start-fullscreen');
driver = webdriver.Firefox(service=service, options=options)
driver.get("https://x.com/i/bookmarks")

input("Sign in, fullscreen, and press enter:")

def img_downloader(webC):
    img_url = webC.get_attribute('outerHTML')
    if ('240x240' in img_url) or ('120x120' in img_url):
        print("too small" + img_url)
        return
    img_url = img_url.split('src=')[1].split(' class')[0].replace('"', '').replace('amp;','').replace('360x360','large').replace('small','large').replace('medium','large')
    print(img_url)
    req = requests.get(img_url)
    name = img_url.split('?')[0].split('/')[-1]
    form = img_url.split('format=')[-1].split('&')[0]
    f = open('temp/'+name+'.'+form, 'wb')
    f.write(req.content)
    f.close()
    

def gif_downloader(webC):
    img_url = webC.get_attribute('outerHTML')
    img_url = img_url.split('src=')[1].split(' type')[0].replace('"', '')
    req = requests.get(img_url)
    name = img_url.split('?')[0].split('/')[-1]
    f = open('temp/'+name, 'wb')
    f.write(req.content)
   

def video_downloader(webC):
    input("Copy video link, put into twitter downloader of your choice, then press enter.")

            

def isolator(webC):
    for c in webC:
        if len(c.find_elements(By.TAG_NAME, 'img')) != 0:
            img_downloader(c)
        elif len(c.find_elements(By.TAG_NAME, 'source')) != 0:
            video_downloader(c)
        elif len(c.find_elements(By.TAG_NAME, 'video')) != 0:
            gif_downloader(c)
        

def click_bookmark(webC):
    bm = webC.find_element(By.CSS_SELECTOR, "[aria-label='Bookmarked']")
    bm.click()
            


while(True):
    try:
        content1 = driver.find_elements(By.CLASS_NAME, POST_NAME)
        #content1[0].screenshot('fizz.png')
        content2 = content1[0].find_elements(By.CLASS_NAME, 'css-175oi2r.r-1pi2tsx.r-1ny4l3l.r-1loqt21')
        if len(content2) == 0:
            content2 = content1[0].find_elements(By.CLASS_NAME, 'css-175oi2r.r-9aw3ui.r-1s2bzr4')
    

        if len(content2) == 0:
            video_downloader(content2)
    #continue
        else:
            isolator(content2)
    

        click_bookmark(content1[0])
        time.sleep(1)
        #input("press enter to continue.")
    
    except Exception as e:
        input("An error occured!" +str(e)+ "fix the error then press enter to continue.")
        continue
    

