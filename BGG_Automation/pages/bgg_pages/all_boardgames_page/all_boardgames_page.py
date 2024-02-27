from BGG_Automation.base.base_driver import Page
from BGG_Automation.pages.bgg_pages.all_boardgames_page.all_boardgames_locators import AllBoardGamesLocators as Locs
import allure


class AllBoardsPage(Page):
    @allure.step('1 step')
    def fill_and_go_next(self):
        self.results(10)

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
            self.filter_digits()

    def all_pages(self):
        return self.find_element(Locs.last_page_number()).text

    def filter_digits(self):
        num = ''
        for char in self.all_pages():
            if char.isdigit():
                num += char
        return int(num)


