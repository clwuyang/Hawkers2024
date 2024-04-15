from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
options.add_argument("--disable-notifications")
options.add_argument("--lang=en-GB")

driver = webdriver.Chrome(options=options)
url = 'https://www.tripadvisor.com/Attraction_Review-g35805-d103239-Reviews-The_Art_Institute_of_Chicago-Chicago_Illinois.html'
driver.get(url)

try:
    WebDriverWait(driver, 20).until(  # Increased timeout to 20 seconds
        EC.presence_of_element_located((By.CLASS_NAME, 'review-container'))  # Ensure this class name is correct
    )
except TimeoutException:
    print("Timed out waiting for page to load")
    driver.quit()

# Further processing and file operations as before

# Get page source after JavaScript execution
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# Extract comments
comments = soup.findAll('div', class_='review-container')
with open('tripadvisor_comments.txt', 'w', encoding='utf-8') as file:
    for comment in comments:
        user_comment = comment.find('p', {'class': 'partial_entry'}).text
        file.write(user_comment + '\n\n')

driver.quit()  # Important to close the driver
