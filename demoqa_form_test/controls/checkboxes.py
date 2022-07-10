from selene.core.entity import Element


class Checkboxes:
    def __init__(self):
        element: Element = ...

    def check(self, *elements):
        for el in elements:
            el.click()