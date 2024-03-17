from BGG_Automation.base.base_driver import Page
from BGG_Automation.pages.bgg_pages.all_boardgames_page.all_boardgames_locators import AllBoardGamesLocators as Locs
from BGG_Automation.utils.excel_handling.save_to_xl import SaveToXl as XlHandling
from BGG_Automation.utils.logger.logger import Logger
import allure


class AllBoardsPage(Page):
    @allure.step('1 step')
    def fill_and_go_next(self):
        self.save_results()

    def next_page_button(self, page_number):
        self.wait_until_element_clickable(Locs.next_page_button(page_number))

    # def results_not_logged_in(self, amount_of_pages):
    #     game_data = []
    #     result_number = 0
    #     for page_number in range(amount_of_pages):
    #         for iteration_value in range(1, 101):
    #             game_data.append([iteration_value + result_number])
    #             self.wait_until_element_located(Locs.results_name(iteration_value))
    #             game_data[iteration_value + result_number - 1].append(
    #                 self.get_texts(Locs.results_name(iteration_value)))
    #             game_data[iteration_value + result_number - 1].append(self.get_link(Locs.results_name(iteration_value)))
    #             rating_results = self.get_texts2(Locs.results_rating(iteration_value))
    #             for i in range(3):
    #                 game_data[iteration_value + result_number - 1].append(rating_results[i])
    #         result_number += 100
    #         self.next_page_button(page_number + 2)
    #         # NumbersHandling.filter_digits(self.all_pages())
    #         XlHandling.save_to_xl(game_data)

    def results_logged_in(self, amount_of_pages):
        game_data = []
        result_number = 0
        for page_number in range(amount_of_pages):
            for iteration_value in range(1, 201, 2):
                game_data.append([int((iteration_value + result_number) / 2 + 1)])
                self.wait_until_element_located(Locs.results_name(iteration_value))
                game_data_iv = int((iteration_value + result_number - 1) / 2)
                game_data[game_data_iv].append(
                    self.get_texts(Locs.results_name(iteration_value)))
                game_data[game_data_iv].append(
                    self.get_link(Locs.results_name(iteration_value)))
                rating_results = self.get_texts2(Locs.results_rating_logged_in(iteration_value))
                for i in range(3):
                    game_data[game_data_iv].append(rating_results[i])
            result_number += 200
            self.next_page_button(page_number + 2)
            # NumbersHandling.filter_digits(self.all_pages())
            return game_data

    def save_results(self):
        XlHandling.save_ranking_to_xl(self.results_logged_in(1))
        Logger.log().info('saved game data to Excel')

    def all_pages(self):
        return self.find_element(Locs.last_page_number()).text
