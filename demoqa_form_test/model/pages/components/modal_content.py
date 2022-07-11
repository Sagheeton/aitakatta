from selene.support.conditions import have
from selene.support.shared.jquery_style import s

from demoqa_form_test.data.student import Student
from demoqa_form_test.model.pages.components.table import Table


class ModalContent:
    def __init__(self, student: Student):
        self.student = student

    def check_content(self):
        Table(s('.table')).get_cell(1, 2).should(have.exact_text('Name Surname'))
        Table(s('.table')).get_cell(2, 2).should(have.exact_text('email@gmail.com'))
        Table(s('.table')).get_cell(3, 2).should(have.exact_text('Male'))
        Table(s('.table')).get_cell(4, 2).should(have.exact_text('8800200060'))
        Table(s('.table')).get_cell(5, 2).should(have.exact_text('31 January,1989'))
        Table(s('.table')).get_cell(6, 2).should(have.exact_text('Chemistry, Maths'))
        Table(s('.table')).get_cell(7, 2).should(have.exact_text('Sports, Music'))
        Table(s('.table')).get_cell(8, 2).should(have.exact_text('e85.jpg'))
        Table(s('.table')).get_cell(9, 2).should(
            have.exact_text('some street somewhere over there wherever it would be, 11, 48')
        )
        Table(s('.table')).get_cell(10, 2).should(have.exact_text('Uttar Pradesh Merrut'))
        return self
