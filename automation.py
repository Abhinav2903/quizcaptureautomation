import time
import csv
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Function to read config file
def read_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Settings']

# Function to navigate through questions and capture results
def navigate_and_capture_results(url):
    # Open the webpage
    driver.get(url)

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button--big")))

    # Locate and click the start button
    # driver.find_element(By.CLASS_NAME,"button--big")
    start_button = driver.find_element(By.CLASS_NAME,"button--big")
    start_button.click()

    # Wait for the page to load
    time.sleep(2)

    # Open CSV file for storing results
    with open('results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Response"])

        # Loop through questions
        while True:
            # Find and print the question text
            question_text = driver.find_element(By.CLASS_NAME,"theses__text").text
            print("Question:", question_text)
            response_value = '1' 
            # Simulate user's response (parameterization)
            response_button = driver.find_element(By.XPATH, f"//*[@id='theses-slider']/div[1]/ol/li[1]/div/div/div/div[2]/ul/li[1]/button]")

            # Click the button
            response_button.click()
    

            # Write question and response to CSV
            writer.writerow([question_text, response_value])

            # Check if it's the last question
            if "Ergebnis" in question_text:
                break

            # Move to the next question
            next_button = driver.find_element("button-text")
            next_button.click()

            # Wait for the page to load
            time.sleep(2)

# Read settings from config file
settings = read_config()
print(settings)
# Define response mappings



# Set Chrome options
chrome_options = webdriver.ChromeOptions()

# Initialize Chrome driver with the specified path
# driver = webdriver.Chrome(service=webdriver.chrome.service.Service(executable_path=settings['webdriver_path']), options=chrome_options)
driver = webdriver.Chrome()

# driver = webdriver.Chrome()
# driver.get("https://www.google.com")
# Call the function to navigate and capture results
navigate_and_capture_results(url=settings['url'])

# Close the browser
driver.quit()
