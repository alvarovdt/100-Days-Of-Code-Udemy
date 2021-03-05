from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
chrome_driver_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

#article_count = driver.find_element_by_id("articlecount")
# article_count = driver.find_elements_by_css_selector(".articlecount a")
# print(article_count.text)

# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
#driver.close()