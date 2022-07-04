from typing import Optional

from selene import command, have
from selene.core.entity import Element
from selene.support.shared import browser


def choose(element: Element, /, *, option: str, by_pressing_tab: Optional [bool] = False):
    if by_pressing_tab:
        element.type(option).press_tab()
    else:
        element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


'''
# in place of two different  (KISS in one word):


def select(element: Element, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def autocomplete(element: Element, /, *, option: str):
    element.type(option).press_enter()
'''
