from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://www.rogerebert.com/'
VALID_BYLINES = [
    "Roger Ebert",
    "Roger Ebert's Ghost",
]
WORKSPACE_DIR = Path(__file__).resolve().parent.parent.absolute()


@pytest.fixture(scope='module', params=['chrome'])
def browser(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_extension(WORKSPACE_DIR / 'dist' / 'chrome.zip')
        browser = webdriver.Chrome(options=chrome_options)
    else:
        raise ValueError(f"Invalid browser: {request.param}")

    yield browser

    browser.close()


class TestRogerEbert:
    @pytest.mark.parametrize('page', [''])
    def test_homepage_js(self, browser, page):
        browser.get(BASE_URL + page)

        review_overlays = browser.find_elements(
            by=By.CLASS_NAME,
            value='review-overlay--author',
        )

        assert len(review_overlays) > 0

        for elem in review_overlays:
            assert elem.text.strip() in VALID_BYLINES

    @pytest.mark.parametrize('page', [
        'reviews/titane-movie-review-2021',
        'reviews/the-human-centipede-2010',
    ])
    def test_review_js(self, browser, page):
        browser.get(BASE_URL + page)

        byline = browser.find_element(
            by=By.CLASS_NAME,
            value='byline',
        )

        assert byline.text.strip() in VALID_BYLINES

    @pytest.mark.parametrize('page', [
        '',
        'reviews',
        'collections//the-best-horror-movies-2021'
    ])
    def test_reviews_list_js(self, browser, page):
        browser.get(BASE_URL + page)

        review_list = browser.find_elements(
            by=By.CLASS_NAME,
            value='review-stack--byline',
        )

        assert len(review_list) > 0

        for elem in review_list:
            assert elem.text.strip() in VALID_BYLINES

    @pytest.mark.parametrize('page', ['collections'])
    def test_collections_list_js(self, browser, page):
        browser.get(BASE_URL + page)

        blog_list = browser.find_elements(
            by=By.CLASS_NAME,
            value='blog-stack--byline',
        )

        assert len(blog_list) > 0

        for elem in blog_list:
            assert elem.text.strip() in VALID_BYLINES
