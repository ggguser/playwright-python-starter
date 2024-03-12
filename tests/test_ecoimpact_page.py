from playwright.sync_api import expect

import config
import pages


class TestEcoimpact:

    def test_ecoimpact_calc(self, page):
        body = '{"result": {"blocks": {"personalImpact": {"data": {"energy": 1000000}}}}}'
        page.route(
            config.url.ECOIMPACT_HANDLER_URL,
            lambda route: route.fulfill(status=200, body=body))
        pages.ecoimpact_page.open_ecoimpact_page(page)
        pages.ecoimpact_page.make_ecoimpact_screenshot('test2', page)


