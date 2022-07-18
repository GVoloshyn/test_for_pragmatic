import time

HOME = '//*[@title="Home"]'
CLIENT_HUB = '//*[@id="menu-item-23582"]//*[contains(text(),"Client Hub")]'
NEWS = '//*[@id="menu-item-9841"]//*[contains(text(),"News")]'
CONTACT = '//*[@id="menu-item-1820"]//*[contains(text(),"Contact")]'
PRODUCTS = '//*[@id="menu-item-200"]//*[contains(text(),"Products")]'
BINGO = '//*[@id="menu-item-11081"]//*[contains(text(),"Bingo")]'

ORANGE_COLOR = 'rgb(255, 128, 14)'
WHITE_COLOR = 'rgb(255, 255, 255)'

JPT_ROOM = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "The Jackpot Room")]'
BNG_BLAST = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "Bingo Blast")]'
REELS_ROOM = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "Reels Room")]'
CNTR_ROADS = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "Country Roads")]'
ZM_ROOM = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "Zoom Room")]'
BOOMBOX = 'body > div.gp__content > section > div.games > div.container > div.live-bingo.row.slick-initialized.slick-slider > div.slick-list.draggable > div > div.slick-slide.slick-current.slick-active > div > div > p'
SW_BANABZA_BNGO = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "Sweet Bonanza Bingo")]'
SNWBALL_BLAST = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "Snowball Blast")]'
ROCK_N_SWING = '//*[@class="slick-slide slick-current slick-active"]//*[contains(text(), "Rock N Swing")]'
RIGHT_ARROW = '//*[@class="right-arrow slick-arrow"]'


def test_example_is_working(page):
    page.goto("https://www.pragmaticplay.com/en")
    page.locator("text=Yes, I am 18 years or older").click()
    home_btn = page.locator(HOME)
    home_btn.hover()
    color_home = home_btn.evaluate("(element) => window.getComputedStyle(element).color")
    assert color_home == WHITE_COLOR
    client_hub_btn = page.locator(CLIENT_HUB)
    client_hub_btn.hover()
    color_ch = client_hub_btn.evaluate("(element) => window.getComputedStyle(element).color")
    assert color_ch == ORANGE_COLOR
    news_btn = page.locator(NEWS)
    news_btn.hover()
    color_news_btn = news_btn.evaluate("(element) => window.getComputedStyle(element).color")
    assert color_news_btn == ORANGE_COLOR
    contact_btn = page.locator(CONTACT)
    contact_btn.hover()
    color_contact_btn = contact_btn.evaluate("(element) => window.getComputedStyle(element).color")
    assert color_contact_btn == ORANGE_COLOR
    page.locator(PRODUCTS).click()
    bingo_btn = page.locator(BINGO)
    bingo_btn.hover()
    color_bingo_btn = bingo_btn.evaluate("(element) => window.getComputedStyle(element).color")
    assert color_bingo_btn == ORANGE_COLOR


def test_second(page):
    page.goto("https://www.pragmaticplay.com/en")
    page.locator("text=Yes, I am 18 years or older").click()
    page.locator(PRODUCTS).click()
    bingo_btn = page.locator(BINGO)
    bingo_btn.click()
    time.sleep(1)
    page.locator(JPT_ROOM).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(BNG_BLAST).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(REELS_ROOM).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(CNTR_ROADS).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(ZM_ROOM).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(BOOMBOX).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(SW_BANABZA_BNGO).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(SNWBALL_BLAST).hover()
    page.locator(RIGHT_ARROW).click()
    time.sleep(1)
    page.locator(ROCK_N_SWING).hover()
    page.locator(RIGHT_ARROW).click()
