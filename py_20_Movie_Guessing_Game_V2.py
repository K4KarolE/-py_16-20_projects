''' Movie Guessing Game V2

- pick a random title from the MoviePY excel sheet
- search for it on Imdb.com
- give back the plot of the movie
- asking the user to guess the title
- give hint/help(director, release year, stars..) if the user needed '''


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://duckduckgo.com/')


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q' ))
    )

except:
    driver.quit()

search = driver.find_element(By.NAME,'q')
search.send_keys('IMDb Forrest gump')
search.send_keys(Keys.RETURN)

search = driver.find_element(By.ID,'r1-0')
search.click()

search = driver.find_element(By.CLASS_NAME,'sc-16ede01-6 cXGXRR')
# print(search.text)




# driver.get('https://duckduckgo.com/')
# search = driver.find_element(By.ID,'searchbox_input')










time.sleep(5)

driver.quit()