from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.baidu.com')

print(driver.find_element_by_id('css_index_result').text)
print(driver.page_source)

driver.close()