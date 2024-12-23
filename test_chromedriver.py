from selenium import webdriver

# Initialize ChromeDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Print page title
print("Page title:", driver.title)

# Keep the browser open for a few seconds
import time
time.sleep(5)

# Close the browser
driver.quit()
