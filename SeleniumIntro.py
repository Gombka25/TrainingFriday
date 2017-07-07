from selenium.webdriver import Edge
from selenium.webdriver import Firefox
#edge = Edge(executable_path=r"C:\Users\U112918\Downloads\MicrosoftWebDriver.exe")
driver = Edge()

driver.get("http://www.wykop.pl")
element = driver.find_element_by_partial_link_text("kompresja") Lapie tylko tytul linka, nie href#<a title="1K17 Kompresja - radziecki pojazd uzbrojony w lasery" href="https://www.wykop.pl/link/3816569/1k17-kompresja-radziecki-pojazd-uzbrojony-w-lasery/">1K17 Kompresja - radziecki pojazd uzbrojony w lasery</a>
element.click()

assert "Radziecki" in driver.title