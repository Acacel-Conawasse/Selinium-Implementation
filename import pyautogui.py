from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Specify the remote debugging port used when starting Chrome
remote_debugging_port = 9222

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", f"localhost:{remote_debugging_port}")

# Initialize the WebDriver with the specified Chrome options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Assuming you are already on a page with a search box named "search_query"
# Wait for the search box to be ready
time.sleep(4)

# Find the search box
search_box = driver.find_element("name", "search_query")

# Type "Davido" into the search box
search_box.send_keys("Davido")
time.sleep(4)

# Press Enter
search_box.send_keys(Keys.RETURN)
time.sleep(4)

# Wait for user input before closing
input("Press Enter to close the browser...")

# It's important to properly close the browser session
driver.quit()
