from haim_levys_adm_vs_rym.pages.AdmAlbumResults import AdmAlbumResults
from haim_levys_adm_vs_rym.pages.MainAnyDecentMusicPage import MainAnyDecentMusicPage
from haim_levys_adm_vs_rym.pages.MainRateYourMusicPage import MainRateYourMusicPage
from haim_levys_adm_vs_rym.pages.RymAlbumResults import RymAlbumResults
from haim_levys_adm_vs_rym.tests.ResultsComparison import ResultsComparison
from haim_levys_adm_vs_rym.tests.SeleniumBase import SeleniumBase
from haim_levys_adm_vs_rym.tests.Globals import ADM_URL, RYM_URL, SEARCH_LIST


class AlbumsRatingsTest():
    for album in range(len(SEARCH_LIST)):
        base = SeleniumBase()
        driver_for_adm = base.selenium_init(ADM_URL)

        adm_main_page = MainAnyDecentMusicPage(driver_for_adm)
        adm_main_page.search_for_album(SEARCH_LIST[album])
        adm_result_page = AdmAlbumResults(driver_for_adm)
        critics_averaged_rating = adm_result_page.get_album_critics_rating()
        print("\033[1m" + "Album's critics averaged rating is: " + critics_averaged_rating + "\033[0m")

        driver_for_rym = base.selenium_init(RYM_URL)

        rym_main_page = MainRateYourMusicPage(driver_for_rym)
        rym_main_page.search_for_album(SEARCH_LIST[album])
        rym_result_page = RymAlbumResults(driver_for_rym)
        users_averaged_rating = rym_result_page.get_album_users_rating()
        print("\033[1m" + "Album's users averaged rating is: " + str(users_averaged_rating) + "\033[0m")

        ResultsComparison.find_highest_value(critics_averaged_rating, users_averaged_rating)

        album_info = rym_result_page.get_album_info()
        print("\n" + "\033[1m" + "More Info:" + "\033[0m" + "\n" + album_info)
        print("-----------------------------------")









