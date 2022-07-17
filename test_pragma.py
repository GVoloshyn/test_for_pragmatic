

HOME = '//*[@title="Home"]'
CLIENT_HUB = '//*[@id="menu-item-23582"]//*[contains(text(),"Client Hub")]'
NEWS = '//*[@id="menu-item-9841"]//*[contains(text(),"News")]'
CONTACT = '//*[@id="menu-item-1820"]//*[contains(text(),"Contact")]'
PRODUCTS = '//*[@id="menu-item-200"]//*[contains(text(),"Products")]'
BINGO = '//*[@id="menu-item-11081"]//*[contains(text(),"Bingo")]'

ORANGE_COLOR = 'rgb(255, 128, 14)'
WHITE_COLOR = 'rgb(255, 255, 255)'


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

