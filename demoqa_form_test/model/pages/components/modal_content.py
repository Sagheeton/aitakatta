from selene.support.conditions import have
from selene.support.shared.jquery_style import s

from demoqa_form_test.data.student import Student
from demoqa_form_test.model.pages.components.table import Table


class ModalContent:
    def __init__(self, student: Student):
        self.student = student

    @property
    def check_content(self):
        st = self.student
        Table(s('.table')).get_cell(1, 2).should(have.exact_text(f'{st.first_name} {st.last_name}'))
        Table(s('.table')).get_cell(2, 2).should(have.exact_text(st.email))
        Table(s('.table')).get_cell(3, 2).should(have.exact_text(st.gender.name.title()))
        Table(s('.table')).get_cell(4, 2).should(have.exact_text(st.mobile_number))
        Table(s('.table')).get_cell(5, 2).should(have.exact_text('31 January,1989'))
        Table(s('.table')).get_cell(6, 2).should(have.exact_text(', '.join(st.subjects)))
        Table(s('.table')).get_cell(7, 2).should(have.exact_text(', '.join(st.hobbies)))
        Table(s('.table')).get_cell(8, 2).should(have.exact_text('e85.jpg'))
        Table(s('.table')).get_cell(9, 2).should(
            have.exact_text(st.current_address)
        )
        Table(s('.table')).get_cell(10, 2).should(have.exact_text(f'{st.state} {st.city}'))
        return self
