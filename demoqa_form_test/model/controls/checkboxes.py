from selene.core.entity import Element


class Checkboxes:
    @staticmethod
    def check(element: Element):
        element.click()