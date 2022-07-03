from selene import command, have
from selene.core.entity import SeleneElement
from selene.support.shared import browser

from selene.support.shared.jquery_style import s


def test_form():
    browser.open('/automation-practice-form')

    s('#firstName').type('Name')
    s('#lastName').type('Surname')
    s('#userEmail').type('email@gmail.com')

    gender_male = s('[for="gender-radio-1"]')
    gender_male.click()

    s('#userNumber').type('88002000600')

    s('#dateOfBirthInput').click()
    s('[class*="month-select"]').click().element('[value="0"]').click()
    s('[class*="year-select"]').click().element('[value="1989"]').click()
    s(f'[class*="datepicker__day--0{31}"]').click()

    s('#subjectsInput').send_keys('m').hover()
    subject_maths = s('#react-select-2-option-0')
    subject_maths.click()

    hobbies_sports = s('[for="hobbies-checkbox-1"]')
    hobbies_sports.click()
    hobbies_music = s('[for="hobbies-checkbox-2"]')
    hobbies_music.click()

    import demoqa_form_test
    from pathlib import Path
    path_to_img = str(Path(demoqa_form_test.__file__).parent.parent.joinpath('resources/e85.jpg'))
    s('[id="uploadPicture"]').send_keys(path_to_img)

    s('[id="currentAddress"]').type("some street somewhere over there wherever it would be, 11, 48")

    def select_by_choosing(element: SeleneElement, /, *, option: str):
        element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()

    def select_by_autocomplete(element: SeleneElement, /, *, option: str):
        element.type(option).press_enter()

    select_by_choosing(s('#state'), option='Uttar Pradesh')

    city = s('[id*="select-4"]')
    select_by_autocomplete(city, option='Merrut')

    s('#submit').perform(command.js.click)
