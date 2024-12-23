from selenium import webdriver

# Set up ChromeDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Print the page title
print("Page Title:", driver.title)

# Close the browser
driver.quit()
