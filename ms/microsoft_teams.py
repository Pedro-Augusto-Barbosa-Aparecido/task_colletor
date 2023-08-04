from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.waiter import Wait


class MicrosoftTeams:
    MICROSOFT_TEAMS_LOGIN_URL = r"https://login.microsoftonline.com/"

    def __init__(self, email: str, password: str):
        self.browser = Chrome()
        self.wait_time = Wait(self.browser)

        self.email = email
        self.password = password

        self._login()

    def __del__(self):
        self.browser.quit()

    def _login(self):
        self.browser.get(MicrosoftTeams.MICROSOFT_TEAMS_LOGIN_URL)

        self.wait_time.long.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo")))

        self.wait_time.long.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR, "input[type=email]"
                )
            )
        ).send_keys(self.email)
        self._click_on_submit()

        self.wait_time.long.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#bannerLogo")))

        self.wait_time.long.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR, "input[type=password]"
                )
            )
        ).send_keys(self.password)
        self._click_on_submit()

    def _click_on_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, "input[type=submit]").click()
