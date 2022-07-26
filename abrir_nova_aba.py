from time import sleep
from selenium import webdriver 

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.google.com/")

# Abre uma nova aba 
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
driver.execute_script("window.open('http://stackoverflow.com/', '_blank')")

# Carrega a nova aba
driver.switch_to_window(driver.window_handles[1])

# Fecha a aba
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 
driver.close()
