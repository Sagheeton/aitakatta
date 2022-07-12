from selene.core import command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

from demoqa_form_test import utils
from demoqa_form_test.data.student import Student
from demoqa_form_test.model.controls.checkboxes import Checkboxes
from demoqa_form_test.model.controls.datepicker import DatePicker
from demoqa_form_test.model.controls.dropdown import Dropdown
from demoqa_form_test.model.controls.tags_input import TagsInput


class StudentRegistrationPage:
    def __init__(self, student: Student):
        self.student = student

    @property
    def open_form(self):
        browser.open('/automation-practice-form')
        return self

    @property
    def fill_form(self):
        st = self.student
        s('#firstName').type(st.first_name)
        s('#lastName').type(st.last_name)
        s('#userEmail').type(st.email)
        s(f'[for="gender-radio-{st.gender}"]').click()
        s('#userNumber').type(st.mobile_number)
        DatePicker(s('#dateOfBirthInput')).set_by_clicking(st.date_of_birth)

        for subject in st.subjects:
            TagsInput(s('#subjectsInput')).add(from_=subject)

        for hobby in st.hobbies:
            Checkboxes().check(s(f'[for="hobbies-checkbox-{hobby}"]'))

        s('[id="uploadPicture"]').send_keys(
            utils.get_full_file_path(relaive_path=st.picture_path)
        )

        s('[id="currentAddress"]').type(st.current_address)

        Dropdown(s('#state')).choose(st.state)
        Dropdown(s('#city')).choose(st.city, by_pressing_tab=True)
        return self

    @property
    def submit_form(self):
        s('#submit').perform(command.js.click)
        return self


