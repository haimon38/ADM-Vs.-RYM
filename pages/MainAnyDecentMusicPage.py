from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class MainAnyDecentMusicPage():

    def __init__(self, driver):
        self.driver = driver
        self.search = self.driver.find_element(By.CSS_SELECTOR, "input[type='text']")
        print("Any Decent Music - Albums ratings by critics")

    def search_for_album(self, text_to_search):
        self.search.click()
        self.search.send_keys(text_to_search)
        self.search.send_keys(Keys.ENTER)
        print(f"Album tested: '{text_to_search}'")
