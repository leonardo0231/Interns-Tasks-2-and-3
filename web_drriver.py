from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


brands = [
    'ASUS',
    'MSI',
    'HP',
    'Lenovo',
    'Dell',
    'Acer',
    'SAMSUNG',
    'Gigabyte',
    'Apple',
    'LG'
]
for i in brands:
    print(i)
brand = input('enter brand: ')


PATH = './chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get('https://www.amazon.com/')

search = driver.find_element(By.NAME, "field-keywords")
search.send_keys('gaming laptop')
search.send_keys(Keys.RETURN)

driver.find_element(By.LINK_TEXT, 'ASUS').click()

product_links = driver.find_elements(
    By.XPATH,
    '//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]',
)

links = []
for link in product_links:
    links.append(link.get_attribute('href'))

products = []
for link in links:
    driver.execute_script("window.open('%s', '_blank')" % link)
    driver.switch_to.window(driver.window_handles[-1])

    product_title = driver.find_element(By.ID, 'titleSection')
    products.append(product_title.text)

    try:
        product_price = driver.find_element(By.CLASS_NAME, "a-price")
        products.append(product_price.text)
    except:
        product_price = None


    products.append(link)

with open('Links.txt', 'w') as f:
    for product in products:
        f.write(product)

driver.quit()