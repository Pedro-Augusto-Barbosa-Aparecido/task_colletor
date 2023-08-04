from typing import Literal

from selenium.common import ElementNotVisibleException, ElementNotSelectableException, TimeoutException
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from exceptions.finder import InvalidStrategy


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

    def click_when_element_is_visible(
            self,
            selector: str,
            by: By = By.XPATH,
            wait_strategy: Literal["normal", "short", "long"] = "normal",
    ):
        match wait_strategy:
            case "short":
                pass
            case "normal":
                pass
            case "long":
                pass
            case _:
                raise InvalidStrategy(
                    "Invalid strategy, please choose some one them: ['short', 'normal', 'long']"
                )
