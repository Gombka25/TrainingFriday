from selenium.webdriver import Edge
from selenium.webdriver import Firefox

# edge = Edge(executable_path=r"C:\Users\U112918\Downloads\MicrosoftWebDriver.exe")
driver = Edge()

# Selenium musi miec wskazanie w jakim iFrame jest szukany element (jesli w ogole jest iFrame)

driver.get("http://igame.com/eye-test/")
driver.switch_to.frame(driver.find_element_by_tag_name("Iframe"))
element = driver.find_element_by_class_name("thechosenone")
for i in range(900):
    element = driver.find_element_by_class_name("thechosenone")
    element.click()