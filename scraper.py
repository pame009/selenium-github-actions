from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Using ChromeDriverManager to download the appropriate Chrome driver
chrome_driver_path = ChromeDriverManager().install()

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

# Providing the path to the downloaded Chrome driver
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

driver.get('http://nytimes.com')
print(driver.title)

# Don't forget to close the driver when you're done
driver.quit()
