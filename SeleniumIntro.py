from selenium.webdriver import Edge
from selenium.webdriver import Firefox
#edge = Edge(executable_path=r"C:\Users\U112918\Downloads\MicrosoftWebDriver.exe")
Driver = Edge()

Driver.get("http://www.allegro.pl")
search_bar = Driver.find_element_by_id("main-search-text")
search_bar.send_keys("Reanult Laguna")
search_bar.click()