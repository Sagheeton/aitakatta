from typing import Optional
from selene import have
from selene.core.entity import Element
from selene.support.shared.jquery_style import ss


class TagsInput:
    def __init__(self, element):
        self.element: Element = element

    def add(self, /, *, from_: str, to: Optional[str] = None):
        if to is None:
            self.element.type(from_).press_tab()
        else:
            self.element.type(from_)
            ss('.subjects-auto-complete__option').element_by(have.text(to or from_)).click()
        return self
