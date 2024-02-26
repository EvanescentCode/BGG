from BGG_Automation.utils.locator_builder.locator_builder import LocatorBuilder as LB


class AllBoardGamesPageLocators:
    LAST_PAGE = LB.xpath('//div[@class="fr"]//a[@title="last page"]')

    @staticmethod
    def next_page_button(page_number):
        return LB.css(f'div[class=fr] a[title="page {str(page_number)}"]')

    @staticmethod
    def results_name(iteration_value):
        name_href_results = LB.css(f'div#results_objectname{iteration_value} a')  # Href + Name
        return name_href_results

    @staticmethod
    def results_rating(iteration_value):
        rating_results = LB.xpath(
            f'//div[@id="results_objectname{iteration_value}"]/../../td[@class="collection_bggrating"]')
        return rating_results

    @staticmethod
    def last_page_number():
        last_page = LB.xpath('//a[@title="last page"]')
        return last_page
