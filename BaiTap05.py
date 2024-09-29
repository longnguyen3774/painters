from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re

# Create an empty dataframe
df = pd.DataFrame({'name': [], 'birth': [], 'death': [], 'nationality': []})

# Webdriver
driver = webdriver.Chrome()

try:
    # Open webpage
    url = 'https://en.wikipedia.org/wiki/List_of_painters_by_name_beginning_with_%22P%22'
    driver.get(url)

    # Wait for 1 second
    time.sleep(1)

    # Get all ul tags
    ul_tags = driver.find_elements(By.TAG_NAME, 'ul')

    # Get ul tag at index 20
    ul_painters = ul_tags[20]  # list start with index=0

    # Get all <li> tags in ul_painters
    li_tags = ul_painters.find_elements(By.TAG_NAME, 'li')

    # Create links
    links = []
    for tag in li_tags:
        try:
            link = tag.find_element(By.TAG_NAME, 'a').get_attribute('href')
            links.append(link)
        except:
            continue

    for link in links:
        driver.get(link)

        # Wait for 0.1 seconds
        time.sleep(0.1)

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
except:
    print('Error!')

# Print df
print(df)

# # Save file
# df.to_excel('painters.xlsx', index=False)
#
# print('DataFrame is written to Excel File successfully.')

driver.quit()
