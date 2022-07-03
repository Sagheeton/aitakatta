from selene import command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from demoqa_form_test.controls import dropdown
from demoqa_form_test.controls import resources
from demoqa_form_test.controls import tags_input


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

    subjects = s('#subjectsInput')
    tags_input.add(subjects, from_='Chem', to='Chemistry')

'''
# My version:

    s('#subjectsInput').send_keys('m').hover()
    subject_maths = s('#react-select-2-option-0')
    subject_maths.click()
'''
    hobbies_sports = s('[for="hobbies-checkbox-1"]')
    hobbies_sports.click()
    hobbies_music = s('[for="hobbies-checkbox-2"]')
    hobbies_music.click()

    path = resources.get_full_file_path(r'resources\e85.jpg')
    s('[id="uploadPicture"]').send_keys(path)

    s('[id="currentAddress"]').type("some street somewhere over there wherever it would be, 11, 48")

    dropdown.choose(s('#state'), option='Uttar Pradesh')

    city = s('[id*="select-4"]')
    dropdown.choose(city, option='Merrut', by_autocomplete=True)

    s('#submit').perform(command.js.click)
