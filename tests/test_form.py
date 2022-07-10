from selene import command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from demoqa_form_test import utils
from demoqa_form_test.controls.checkboxes import Checkboxes
from demoqa_form_test.controls.datepicker import DatePicker
from demoqa_form_test.controls.dropdown import Dropdown
from demoqa_form_test.controls.tags_input import TagsInput


def test_form():
    browser.open('/automation-practice-form')

    s('#firstName').type('Name')
    s('#lastName').type('Surname')
    s('#userEmail').type('email@gmail.com')

    gender_male = s('[for="gender-radio-1"]')
    gender_male.click()

    s('#userNumber').type('88002000600')

    # DatePicker(s('#dateOfBirthInput')).choose_by_typing('31 Jan 1989')
    DatePicker(s('#dateOfBirthInput')).choose_by_clicking(31, 1, 1989)

    subjects = TagsInput(s('#subjectsInput'))
    subjects.add(from_='Chem', to='Chemistry')
    subjects.add(from_='m')

    hobbies = Checkboxes()
    sports = s('[for="hobbies-checkbox-1"]')
    music = s('[for="hobbies-checkbox-3"]')
    hobbies.check(sports, music)

    path = utils.get_full_file_path(relaive_path=r'resources\e85.jpg')
    s('[id="uploadPicture"]').send_keys(path)

    s('[id="currentAddress"]').type("some street somewhere over there wherever it would be, 11, 48")

    Dropdown(s('#state')).choose(option='Uttar Pradesh')

    Dropdown(s('#city')).choose(option='Merrut', by_pressing_tab=True)

    s('#submit').perform(command.js.click)
