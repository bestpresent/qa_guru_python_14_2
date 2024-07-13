from selene import browser, have


def test_valid():
    browser.open('')
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_invalid():
    browser.open('')
    browser.element('[name="q"]').type('mrs_is1').press_enter()
    browser.element('.card-section').should(have.text('Data have not find, sorry'))