from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

website = 'https://clist.by/resource/geeksforgeeks.org/'
s = Service("/home/subhojit/discordbot/pbot/src/chromedriver")

driver = webdriver.Chrome(service=s)

driver.get(website)

# Use WebDriverWait to wait for the tbody element to be present
wait = WebDriverWait(driver, 10)
tbody_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[3]/div[4]/div/table/tbody")))

# Find all rows inside the tbody
rows = tbody_element.find_elements(By.TAG_NAME, 'tr')

# Iterate through each row and print the text content of cells
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')  
    row_data = [cell.text.strip() for cell in cells]
    print(row_data)


driver.quit()

