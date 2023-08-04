from typing import Literal

from selenium.common import ElementNotVisibleException, ElementNotSelectableException, TimeoutException
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

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

        self.browser = browser

    def click_when_element_is_visible(
            self,
            selector: str,
            by: str = By.CSS_SELECTOR,
            wait_strategy: Literal["normal", "short", "long"] = "normal",
    ) -> None:
        self.wait_element_is_visible(
            by=by,
            selector=selector,
            must_be_return_element=True,
            wait_strategy=wait_strategy
        ).click()

    def wait_element_is_visible(
            self,
            selector: str,
            must_be_return_element: bool = False,
            by: str = By.CSS_SELECTOR,
            wait_strategy: Literal["normal", "short", "long"] = "normal",
    ) -> WebElement | None:
        match wait_strategy:
            case "short":
                element = self.short.until(
                    EC.visibility_of_element_located((by, selector))
                )

                if must_be_return_element:
                    return element
                return
            case "normal":
                element = self.normal.until(
                    EC.visibility_of_element_located((by, selector))
                )

                if must_be_return_element:
                    return element
                return
            case "long":
                element = self.long.until(
                    EC.visibility_of_element_located((by, selector))
                )

                if must_be_return_element:
                    return element
                return
            case _:
                raise InvalidStrategy(
                    "Invalid strategy, please choose some one them: ['short', 'normal', 'long']"
                )
