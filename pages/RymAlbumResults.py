from selenium.webdriver.common.by import By


class RymAlbumResults():
    def __init__(self, driver):
        self.driver = driver
        self.album_results = self.driver.find_elements(By.CLASS_NAME, "searchpage")
        self.album_results[0].click()
        self.album_rating = self.driver.find_element(By.CLASS_NAME, "avg_rating")
        self.album_info = self.driver.find_element(By.CLASS_NAME, "album_info")

    def get_album_users_rating(self):
        rating_text = self.album_rating.text
        text_to_float = round(float(rating_text) * 10 / 5, 1)
        return text_to_float

    def get_album_info(self):
        info_text = self.album_info.text
        index = info_text.index("RYM")
        sliced_info_text = info_text[:index]
        return sliced_info_text



