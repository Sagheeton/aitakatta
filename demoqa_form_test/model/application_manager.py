from demoqa_form_test.data.student import Student
from demoqa_form_test.model.pages.components.modal_content import ModalContent
from demoqa_form_test.model.pages.student_registration_page import StudentRegistrationPage


class ApplicationManager:
    def __init__(self, student: Student):
        self.page = StudentRegistrationPage(student)
        self.result = ModalContent(student)

