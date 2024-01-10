from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Selenium WebDriver (make sure you have chromedriver installed)
driver = webdriver.Chrome()
async def getUpcomingContestListgfg():
    # Open the website
    driver.get("https://clist.by/?resource=126&view=list&group=no&status=coming")

    # Wait for the page to load (you may need to adjust the waiting time)
    driver.implicitly_wait(10)

    # Find all div elements with class 'contest row coming'
    contest_elements = driver.find_elements(By.CSS_SELECTOR, 'div.contest.row.coming')

    # Initialize a list to store dictionaries
    contests_data = []

    # Extract and store data from each contest element
    for contest in contest_elements:
        data = {
            "Start Time": contest.find_element(By.CSS_SELECTOR, 'div.start-time').text.strip(),
            "Duration": contest.find_element(By.CSS_SELECTOR, 'div.duration').text.strip(),
            "Time Left": contest.find_element(By.CSS_SELECTOR, 'div.timeleft').text.strip(),
            "Event Title": contest.find_element(By.CSS_SELECTOR, 'span.contest_title').text.strip(),
        }
        contests_data.append(data)

    # Close the WebDriver
    driver.quit()

    # Print the entire list of dictionaries
    '''for contest_data in contests_data:
        print(contest_data)'''
    return(contests_data)    
