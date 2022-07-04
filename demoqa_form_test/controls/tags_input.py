from typing import Optional

from selene import have
from selene.core.entity import Element
from selene.support.shared.jquery_style import ss


def add(element: Element, /, *, from_: str, to: Optional[str] = None):
    if to is None:
        element.type(from_).press_tab()
    else:
        element.type(from_)
        ss('.subjects-auto-complete__option').element_by(have.text(to or from_)).click()

