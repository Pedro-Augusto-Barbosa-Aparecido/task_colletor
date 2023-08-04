from selenium.common import ElementNotVisibleException, ElementNotSelectableException, TimeoutException
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class Wait:
    def __init__(self, browser: WebDriver):
        try:
            self.normal = WebDriverWait(browser, timeout=30, poll_frequency=1,
                                        ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            self.short = WebDriverWait(browser, timeout=10, poll_frequency=1,
                                       ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
            self.long = WebDriverWait(browser, timeout=60, poll_frequency=1,
                                      ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
        except TimeoutException:
            print('Long time to initialize application')
