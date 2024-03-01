from BGG_Automation.utils.locator_builder.locator_builder import LocatorBuilder as LB


class LoginLocators:
    SIGN_IN_INITIALIZE_BUTTON = LB.css(
        'li[class="c-nav-session c-nav-primary-separated dropdown-primary"] a[class="btn"]')
    USERNAME_INPUT = LB.id('inputUsername')
    PASSWORD_INPUT = LB.id('inputPassword')
    SIGN_IN_FINISH_BUTTON = LB.css('button[class="btn btn-lg btn-primary"]')
