from selenium import webdriver
chrome_driver_path = "/usr/bin/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
#driver.get("https://www.amazon.es/Apple-MWP22TY-A-AirPods-Pro/dp/B07ZPNLGDP")
driver.get("https://www.python.org")
#price = driver.find_element_by_id("priceblock_ourprice")
#print(price.text)

# search_bar = driver.find_element_by_name("field-keywords")
# print(search_bar.get_attribute("placeholder"))


# bug_link = driver.find_element_by_xpath('//*[@id="productTitle"]')
# print(bug_link.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
names_times = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": names_times[n].text,
    }
print(events)
driver.close() # close the tab
#driver.quit() # shutdown browser