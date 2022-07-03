#просто импорт браузера
from selene import have, be, by, command
from selene.support.shared import browser
import os

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

    s('[id="state"]').perform(command.js.scroll_into_view).click()
    state_uttar_pradesh = s('[id*="select"][id*="option-1"]')
    state_uttar_pradesh.click()

    s('[id="city"]').click()
    city_merrut = s('[id*="select"][id*="option-2"]')
    city_merrut.perform(command.js.click)

    s('#submit').perform(command.js.click)



