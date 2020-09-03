from selenium import webdriver

CHROME_DRIVER_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe'
CHROME_BROWSER_PATH = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'

PARSE_URL = 'https://air.pm.by/en/prematch/all/1%7CTT'

chromedriver = CHROME_DRIVER_PATH

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.binary_location = CHROME_BROWSER_PATH

driver = webdriver.Chrome(chromedriver, chrome_options=options)

driver.get(PARSE_URL)

items = driver.find_elements_by_tag_name('prematch-block')

for item in items:
    print('Line:(\n{}\n)'.format(item.text))

driver.close()