from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

# Create an empty dataframe
df = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Webdriver
driver = webdriver.Chrome()

# Open webpage
url = 'https://en.wikipedia.org/wiki/Edvard_Munch'
driver.get(url)

# Wait for 1 second
time.sleep(1)

# Get name
try:
    name = driver.find_element(By.TAG_NAME, 'h1').text
except:
    name = ''

# Get birthday
try:
    birth_element = driver.find_element(By.XPATH, "//th[text()='Born']/following-sibling::td")
    birth = birth_element.text
    birth = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', birth)[0]
except:
    birth = ''

# Get death
try:
    death_element = driver.find_element(By.XPATH, "//th[text()='Died']/following-sibling::td")
    death = death_element.text
    death = re.findall(r'[0-9]{1,2}+\s+[A-Za-z]+\s+[0-9]{4}', death)[0]
except:
    death = ''

# Get nationality
try:
    nationality_element = driver.find_element(By.XPATH, "//th[text()='Nationality']/following-sibling::td")
    nationality = nationality_element.text
except:
    nationality = ''

# Create painter's info dictionary
painter = {'name': name, 'birth': birth, 'death': death, 'nationality': nationality}

# Convert to dataframe
painter_df = pd.DataFrame([painter])

# Add to df
df = pd.concat([df, painter_df], ignore_index=True)

# Print df
print(df)

driver.quit()
