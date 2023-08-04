import time

from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from utils.iframe_mgt import IFrameManagement
from utils.waiter import Wait


class MicrosoftTeams:
    MICROSOFT_TEAMS_LOGIN_URL = r"https://teams.microsoft.com/_#/school/teams-grid/General?ctx=teamsGrid"

    def __init__(self, email: str, password: str):
        self.browser = Chrome()
        self.wait_time = Wait(self.browser)
        self.iframe_mgt = IFrameManagement(self.browser)

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
        self._move_to_assignment_screen()

        try:
            self.wait_time.wait_element_is_visible(
                '//*[@id="root"]/div/div/div/div/div/div[2]',
                by=By.XPATH,
                wait_strategy="long",
            )

            print("Não tem tarefa para fazer!")
        except Exception:
            pass

        self.iframe_mgt.go_out_iframe()

    def get_home_works_pending(self):
        self._move_to_assignment_screen()

        self.iframe_mgt.go_out_iframe()

    def get_home_works_completed(self):
        self._move_to_assignment_screen()

        self.iframe_mgt.go_out_iframe()

    def _check_if_has_home_works(self):
        pass

    def _move_to_assignment_screen(self):
        self.wait_time.click_when_element_is_visible(
            "#teams-app-bar > ul > li:nth-child(4) button",
            wait_strategy="long"
        )

        self.iframe_mgt.enter_in_iframe(
            "/html/body/app-caching-container/div/div/extension-tab/div/embedded-page-container/div/iframe"
        )

    def _click_on_submit(self):
        self.wait_time.click_when_element_is_visible("input[type=submit]", by=By.CSS_SELECTOR)

    def _wait_school_banner(self):
        self.wait_time.long.until(
            EC.visibility_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#bannerLogo"
                )
            )
        )
