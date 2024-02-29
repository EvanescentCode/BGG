from BGG_Automation.utils.locator_builder.locator_builder import LocatorBuilder as LB


class CommonPageLocators:
    COOKIES_ACCEPT = LB.css('button[class="fc-button fc-cta-consent fc-primary-button"]')
    PRIVACY_ACCEPT = LB.id('c-p-bn')
    BROWSE_DROPDOWN = LB.xpath('//button[contains(text(), "Browse")]')
    ALL_BOARDGAMES_BUTTON = LB.xpath('//a[contains(text(), "All Boardgames")]')
    CATEGORIES_BUTTON = LB.xpath('//a[contains(text(), "Categories")]')
    ARTISTS_BUTTON = LB.xpath('//a[contains(text(), "Artists")]')
    PUBLISHERS_BUTTON = LB.xpath('//a[contains(text(), "Publishers")]')
    HONORS_BUTTON = LB.xpath('//a[contains(text(), "Honors")]')
    GONE_CARDBOARD_BUTTON = LB.xpath('//a[contains(text(), "Gone Cardboard")]')
    FAMILIES_BUTTON = LB.xpath('//a[contains(text(), "Families")]')
    MECHANICS_BUTTON = LB.xpath('//a[contains(text(), "Mechanics")]')
    DESIGNERS_BUTTON = LB.xpath('//a[contains(text(), "Designers")]')
    RANDOM_GAME_BUTTON = LB.xpath('//a[contains(text(), "Random Game")]')


