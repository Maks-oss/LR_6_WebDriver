import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

web = webdriver.Chrome(ChromeDriverManager().install())
web.get('https://bigtoys.ua/')
search_input = 'обод'
web.find_element_by_name('search').send_keys(search_input)
time.sleep(3)
web.find_element_by_class_name('btnsrch').send_keys(Keys.RETURN)
time.sleep(3)
actual_result = web.find_element_by_tag_name('h1').text
assert search_input in actual_result
results = web.find_element_by_css_selector('.category-products').find_elements_by_class_name('category-product')
assert len(results) > 0
print(actual_result, len(results))
