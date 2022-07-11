from selene.support.shared import browser
from selene.core.entity import Element
from selene.support.shared.jquery_style import s, ss

from demoqa_form_test.data.date import Date


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def set_by_clicking(self, date: Date):
        self.element.click()
        s('[class*="month-select"]').click().element(f'[value="{date.month-1}"]').click()
        s('[class*="year-select"]').click().element(f'[value="{date.year}"]').click()
        s(f'[class*="datepicker__day--0{date.day}"]').click()

    '''
    This one only works in some specific conditions:
    
    
    def set_by_typing(self, option: str):
        self.element.click()
        self.element.set_value(option).click()
    '''
