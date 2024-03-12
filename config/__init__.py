from pathlib import Path

from config.url import Url
from config.playwright import Playwright
from config.expectations import Expectations

OUTPUT_DIR = Path('output')

url = Url()
playwright = Playwright()
expectations = Expectations()
