from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

# Automatically install and get the path of chromedriver that matches the installed chrome browser version
chromedriver_autoinstaller.install()


async def getUpcomingContestListgfg():
    # Use ChromeDriverManager to handle the downloading and installation of chromedriver
    data = []
    with webdriver.Chrome() as driver:
        website = "https://clist.by/resource/geeksforgeeks.org/"
        driver.get(website)

        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(
            lambda driver: driver.execute_script("return document.readyState")
            == "complete"
        )

        # Use a more robust XPath
        xpath_tbody = "/html/body/div[4]/div/div[3]/div[4]/div/table/tbody"

        try:
            # Wait for the tbody element to be present
            wait = WebDriverWait(driver, 10)
            tbody_element = wait.until(
                EC.presence_of_element_located((By.XPATH, xpath_tbody))
            )

            # Find all rows inside the tbody
            rows = tbody_element.find_elements(By.TAG_NAME, "tr")

            # Iterate through each row and print the text content of cells
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, "td")
                row_data = [cell.text.strip() for cell in cells]
                # print(row_data)
                data.append(row_data)

        except TimeoutException:
            print("Timed out waiting for the tbody element to be present")

        columns = ["Date", "Event"]

        # Deserialize data into a list of dictionaries
        deserialized_data = [dict(zip(columns, row)) for row in data]

        # Print the deserialized data
        # for row in deserialized_data:
        #   print(row)
        filtered_data = [item for item in deserialized_data if item]
        return filtered_data
