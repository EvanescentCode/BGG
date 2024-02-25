from BGG_Automation.base.base_driver import Page
from BGG_Automation.pages.bgg_pages.all_boardgames_page.all_boardgames_locators import AllBoardGamesPageLocators as Locs
import time


class AllBoardsPage(Page):

    def fill_and_go_next(self):
        self.results()

    def results(self):
        for iteration_value in range(1, 101):
            print(iteration_value)
            self.wait_until_element_located(Locs.results_name(iteration_value))
            print(self.get_texts(Locs.results_name(iteration_value)))
            print(self.get_link(Locs.results_name(iteration_value)))
            rating_results = self.get_texts2(Locs.results_rating(iteration_value))
            for i in range(3):
                print(rating_results[i])
            print('\n')


