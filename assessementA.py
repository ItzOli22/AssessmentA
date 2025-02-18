from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = r"C:\Users\lelia\Downloads\chrome-win64\chrome-win64\chrome.exe"
webdriver_service = Service(r"C:\Users\lelia\Desktop\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

url = 'https://mashable.com/'
driver.get(url)

time.sleep(5)

articles = driver.find_elements(By.CSS_SELECTOR, '.broll_info')

headlines = []
for article in articles:
    try:
        title = article.find_element(By.CSS_SELECTOR, '.caption').text
        date_str = article.find_element(By.CSS_SELECTOR, '.datepublished').text
        article_url = article.find_element(By.TAG_NAME, 'a').get_attribute('href')

        date_obj = datetime.strptime(date_str, '%b. %d, %Y')

        if date_obj >= datetime(2022, 1, 1):
            headlines.append({
                'title': title,
                'link': article_url,
                'date': date_obj
            })
    except Exception as e:
        print(f"Error processing article: {e}")

headlines.sort(key=lambda x: x['date'], reverse=True)

for headline in headlines:
    print(f"Title: {headline['title']}")
    print(f"Link: {headline['link']}")
    print(f"Published on: {headline['date'].strftime('%B %d, %Y')}")
    print("")

driver.quit()
