import time

from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.waiter import Wait


class MicrosoftTeams:
    MICROSOFT_TEAMS_LOGIN_URL = r"https://teams.microsoft.com/_#/school/teams-grid/General?ctx=teamsGrid"

    def __init__(self, email: str, password: str):
        self.browser = Chrome()
        self.wait_time = Wait(self.browser)

        self.email = email
        self.password = password

        self.browser.maximize_window()

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

        self._wait_school_banner()

        self.wait_time.long.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR, "input[type=password]"
                )
            )
        ).send_keys(self.password)
        self._click_on_submit()

        self._wait_school_banner()
        self._click_on_submit()

        time.sleep(10)  # wait a teams load content

    def get_home_works_todo(self):
        pass

    def get_home_works_pending(self):
        pass

    def get_home_works_completed(self):
        pass

    def _click_on_submit(self):
        self.browser.find_element(By.CSS_SELECTOR, "input[type=submit]").click()

    def _wait_school_banner(self):
        self.wait_time.long.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#bannerLogo"
                )
            )
        )
