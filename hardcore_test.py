#просто импорт браузера
from selene import have, be, by, command
from selene.support.shared import browser
import os


name = "Name"
surname = "Surname"

def test_form():
    #наконец открываем браузер
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type(name)
    browser.element('[id="lastName"]').should(be.blank).type(surname)
    browser.element('[id="userEmail"]').should(be.blank).type('email@gmail.com')
    browser.elements('[class="custom-control custom-radio custom-control-inline"]').element(1).click()
    browser.element('[id="userNumber"]').should(be.blank).type('88002000600')
    #выбор даты рождения **********************************************************************************
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="0"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1989"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--031"]').click()
    #*********************************************************************************************************
    browser.element('[id="subjectsInput"]').send_keys('m').hover()
    browser.element('[id="react-select-2-option-0"]').click()
    browser.elements('[class="custom-control custom-checkbox custom-control-inline"]').element(1).click()
    browser.elements('[class="custom-control custom-checkbox custom-control-inline"]').element(2).click()
    browser.element('[id="uploadPicture"]').send_keys(os.getcwd() + "\qa.jpg")
    browser.element('[id="currentAddress"]').type("some street somewhere over there wherever it would be, 11, 48").perform(command.js.scroll_into_view)

    browser.element('[id="state"]').click()
    browser.element('[id="react-select-3-option-0"]').click()
    browser.element('[id="city"]').click()
    browser.element('[id="react-select-4-option-1"]').click()
    browser.element('[id="userEmail"]').submit()

    test_b = browser.all('.table tr td:nth-child(2)')
    for b in test_b:
        print(b.text)

