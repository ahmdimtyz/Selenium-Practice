from selenium import webdriver

# Set up the WebDriver
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Print the title of the page
print("Page title is:", driver.title)

# Close the browser
driver.quit()
