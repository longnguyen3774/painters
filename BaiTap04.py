from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khoi tao Webdriver
driver = webdriver.Chrome()

for i in range(65, 91):
    try:
        # Mo trang
        url = 'https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22'+chr(i)+'%22'
        driver.get(url)

        # Doi mot chut de trang tai
        time.sleep(2)

        # Lay ra tat ca cac the ul
        ul_tags = driver.find_elements(By.TAG_NAME, 'ul')

        # Chon the ul thu 21
        ul_painters = ul_tags[20]  # list start with index=0

        # Lay ra tat ca the <li> thuoc ul_painters
        li_tags = ul_painters.find_elements(By.TAG_NAME, 'li')

        # Tao danh sach cac title
        titles = [tag.find_element(By.TAG_NAME, 'a').get_attribute('title') for tag in li_tags]

        # In ra title
        for title in titles:
            print(title)
    except:
        print('Error')

# Dong webdriver
driver.quit()
