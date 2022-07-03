__author__ = 'miserylab'

from selene import have, command
from selene.core.entity import SeleneElement
from selene.support.shared import browser


class Subjects:
    computer_science = 'Computer Science'
    english = 'English'


def test_student_registration_form():
    browser.open('/automation-practice-form')

    browser.element('.main-header').should(have.exact_text('Practice Form'))
    browser.element('#firstName').type('firstName')
    browser.element('#lastName').type('lastName')
    browser.element('#userEmail').type('test@test.com')
    browser.element("[for='gender-radio-2']").click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element("[value='8']").click()
    browser.element('.react-datepicker__year-select').click().element("[value='1973']").click()
    browser.element('.react-datepicker__day--013').click()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("[for='hobbies-checkbox-3']").click()

    # browser.element('#subjectsInput').type(Subjects.computer_science)
    # browser.all('.subjects-auto-complete__option').element_by(have.text(Subjects.computer_science))
    # browser.element('#subjectsInput').type(Subjects.english)
    # browser.all('.subjects-auto-complete__option').element_by(have.text(Subjects.english))

    def autocomplete(selector: str, /, *, from_: str, to: str = None):
        browser.element(selector).type(from_)
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(to if to is not None else from_))



        '''
       # OR:
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
            to or from_
        ))
       # OR:
        browser.all('.subjects-auto-complete__option').element_by(have.exact_text(
            to if to else from_
        ))
       # OR:
        if to is not None:
            browser.all('.subjects-auto-complete__option').element_by(have.exact_text(to))
        else:
            browser.all('.subjects-auto-complete__option').element_by(have.exact_text(from_))
        '''

    # autocomplete('#subjectsInput', from_='Com', to=Subjects.computer_science)
    # autocomplete('#subjectsInput', from_=Subjects.english)

    # browser.element('#subjectsInput').send_keys('S').hover()

    browser.element('#react-select-2-option-2').click()

    # browser.element('#uploadPicture').send_keys(data('e85.jpg'))

    browser.element('#currentAddress').type('currentAddress')

    select_by('#state', option='Haryana')
    select_by('#city', option='Panipat')

    # browser.element('#state').perform(command.js.scroll_into_view).click()
    # browser.element("#react-select-3-option-2").click()
    # browser.element('#city').perform(command.js.scroll_into_view).click()
    # browser.element('#react-select-4-option-1').perform(command.js.click)

    browser.element('#submit').perform(command.js.click)

    # asserts
    browser.elements('table tr').element(1).should(have.text('firstName lastName'))
    browser.elements('table tr').element(2).should(have.text('test@test.com'))
    browser.elements('table tr').element(3).should(have.text('Female'))
    browser.elements('table tr').element(4).should(have.text('1234567890'))
    browser.elements('table tr').element(5).should(have.text('13 September,1973'))
    browser.elements('table tr').element(6).should(have.text('Computer Science', 'English'))
    browser.elements('table tr').element(7).should(have.text('Reading, Music'))
    browser.elements('table tr').element(8).should(have.text('e85.jpg'))
    browser.elements('table tr').element(9).should(have.text('currentAddress'))
    browser.elements('table tr').element(10).should(have.text('Haryana Panipat'))


def select(element: SeleneElement, /, *, option: str):  # todo: consider option_text
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).perform(command.js.click)


def select_by(selector: str, /, *, option: str):  # todo: consider option_text
    select(browser.element(selector), option=option)
    # browser.element(selector).perform(command.js.scroll_into_view).click()
    # browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).perform(command.js.click)


# def autocomplete(element: SeleneElement, /, *, from_: str, to: Optional[str] = None):
#     element.type(from_)
#     browser.all(
#         '.subjects-auto-complete__option'
#     ).element_by(have.text(to or from_)).click()

def select_dropdown(selector: str, /, *, option: str):
    browser.element(selector).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).perform(command.js.click)
#
#
# def data(relative_path):
#     import demoqa_tests
#     from pathlib import Path
#     return (
#         Path(demoqa_tests.__file__)
#             .parent
#             .parent
#             .joinpath('data/')
#             .joinpath(relative_path)
#             .absolute()
#             .__str__()
#     )


'''Основное задание

1. Применение инструментов Модульной Парадигмы

1.1. Вынести в отдельный модуль функцию-хелпер для трансформации пути к файлу с относительного в абсолютный, реализовав эту функцию, если это еще не сделано.



2. Применение инструментов Объектно-Ориентированной Парадигмы

2.1. Повторить показанное в уроке, создав PageObject для контрола типа «Tags Input». Добавить в "шаблон фабрики" оба способа работы с контролом – через автодополнение по Tab и выбор из списка предложенных вариантов.

2.2. Реализовать PageObject для контрола «Dropdown с автодополнением», с возможностью устанавливать значение для поля как через автодополнение по Tab, так и выбор из списка. 

2.3. Реализовать PageObject для контрола DatePicker с возможностью как установить значение в поле ввода явно, так и выбрать нужную дату из диалога дейтпикера.

2.4. Реализовать PageObject для контрола «Table», использующийся в тесте для проверки результата подтверждения формы.





Бонусное задание (сдавать в отдельной бренче)

1.2* Вместо PageObject реализовать в отдельном модуле функцию для работы с контролом «Tags Input», которая в зависимости от переданных именованых аргументов будет либо автодополнять введенный текст по Tab, либо выбирать по клику из предложенных в списке.'''
