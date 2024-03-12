import time

import pytest
import pages


class TestEcoimpact:

    def test_ecoimpact_calc(self, page):
        pages.ecoimpact_page.open_ecoimpact_page(page)
        pages.ecoimpact_page.make_ecoimpact_screenshot('test2', page)