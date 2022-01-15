from playwright.sync_api import sync_playwright
from playwright.sync_api._generated import Page


class PlaywrightManager:
    __playwright = None
    __browser = None
    __page = None

    @classmethod
    def create_playwright_page(cls):
        cls.__playwright = sync_playwright().start()
        cls.__browser = cls.__playwright.chromium.launch(headless=False, slow_mo=50)
        cls.__page = cls.__browser.new_page()

    @classmethod
    def get_page(cls) -> Page:
        if not cls.__page:
            cls.create_playwright_page()
        return cls.__page

    @classmethod
    def close_page(cls):
        cls.__browser.close()
        cls.__playwright.stop()
