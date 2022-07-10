from typing import Optional

from selene import command, have
from selene.core.entity import Element
from selene.support.shared import browser


class Dropdown:
    def __init__(self, element: Element):
        self.element = element

    def choose(self, /, *, option: str, by_pressing_tab: Optional[bool] = False):
        if by_pressing_tab:
            self.element.element('[id*=-input]').type(option).press_tab()
        else:
            self.element.perform(command.js.scroll_into_view).click()
            browser.all('[id*=select-][id*=-option]').element_by(have.exact_text(option)).click()


'''
# in place of two different  (KISS in one word):


def select(element: Element, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def autocomplete(element: Element, /, *, option: str):
    element.type(option).press_enter()
'''
