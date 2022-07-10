from selene import have, be
from selene.support.shared import browser
from selene.core.entity import Element
from selene.support.shared.jquery_style import s, ss


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def set_by_clicking(self, day: int, month: int, year: int):
        self.element.click()
        s('[class*="month-select"]').click().element(f'[value="{month}"]').click()
        s('[class*="year-select"]').click().element(f'[value="{year}"]').click()
        s(f'[class*="datepicker__day--0{day}"]').click()


    def set_by_typing(self, option: str):
        self.element.click()
        browser.execute_script(
            '''
                document.querySelector("#dateOfBirthInput")
                .value = ''
            ''')
        self.element.set_value(option).click()

