from BGG_Automation.base.base_driver import Page
from BGG_Automation.pages.bgg_pages.all_boardgames_page.all_boardgames_locators import AllBoardGamesPageLocators as Locs
import allure
import time


class AllBoardsPage(Page):
    @allure.step('1 step')
    def fill_and_go_next(self):
        print(self.get_last_page())
        self.results(1)

    def next_page_button(self, page_number):
        self.wait_until_element_clickable(Locs.next_page_button(page_number))

    def results(self, amount_of_pages):
        result_number = 0
        for page_number in range(amount_of_pages):
            for iteration_value in range(1, 101):
                print(iteration_value + result_number)
                self.wait_until_element_located(Locs.results_name(iteration_value))
                print(self.get_texts(Locs.results_name(iteration_value)))
                print(self.get_link(Locs.results_name(iteration_value)))
                rating_results = self.get_texts2(Locs.results_rating(iteration_value))
                for i in range(3):
                    print(rating_results[i])
                print('\n')
            result_number += 100
            self.next_page_button(page_number + 2)

    def get_last_page(self):
        self.get_inner_html(Locs.LAST_PAGE)
