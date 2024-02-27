from BGG_Automation.utils.locator_builder.locator_builder import LocatorBuilder as LB


class GameInsidesLocators:
    RATING_INDICATOR = LB.css('span[itemprop="ratingValue"]')
    COMPLEXITY_WEIGHT_INDICATOR = LB.css('span[class="ng-binding gameplay-weight-medium"]')
    RECOMMENDED_PLAYERS_BUTTON = LB.css('span[item-poll-button="numplayers"] button[class="btn btn-link btn-xs"]')

