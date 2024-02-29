from selenium.webdriver.common.by import By


class AdmAlbumResults():

    def __init__(self, driver):
        self.driver = driver
        self.album_results = self.driver.find_element(By.CSS_SELECTOR, "div[class='results_right']")
        self.album_results.click()
        self.album_rating = self.driver.find_element(By.CSS_SELECTOR, "p[class='score']")

    def get_album_critics_rating(self):
        text = self.album_rating.text
        return text






