from utils.waiter import Wait
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By


class IFrameManagement(Wait):
    def __init__(self, browser: WebDriver):
        super(IFrameManagement).__init__(browser)

    def enter_in_iframe(self, iframe_xpath: str):
        iframe = self.wait_element_is_visible(
            selector=iframe_xpath,
            by=By.XPATH,
            wait_strategy="long"
        )

        self.browser.switch_to.frame(iframe)

    def go_out_iframe(self):
        self.browser.switch_to.default_content()
