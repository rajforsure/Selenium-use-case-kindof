from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)  # Press Enter

# Wait for results to load
time.sleep(2)

# Get search result titles
results = driver.find_elements(By.CSS_SELECTOR, "h3")

# Print the titles
for i, result in enumerate(results[:5], start=1):
    print(f"{i}. {result.text}")

# Close the browser
driver.quit()
