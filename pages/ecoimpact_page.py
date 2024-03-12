from playwright.sync_api import Page
import config


class EcoimpactPage:
    _ECOIMPACT_CALC = ".desktop-wrapper-OutiE"

    def open_ecoimpact_page(self, page: Page) -> None:
        page.goto(config.url.ECOIMPACT_URL)

    def make_ecoimpact_screenshot(self, case_name, page: Page) -> None:
        page.locator(self._ECOIMPACT_CALC).screenshot(path=config.OUTPUT_DIR / f'{case_name}.png')
