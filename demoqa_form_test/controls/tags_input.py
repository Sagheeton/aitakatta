from typing import Optional

from selene import have
from selene.core.entity import SeleneElement
from selene.support.shared.jquery_style import ss


def add(element: SeleneElement, /, *, from_: str, to: Optional[str] = None):
    element.type(from_)
    ss('.subjects-auto-complete__option').element_by(have.text(to or from_)).click()