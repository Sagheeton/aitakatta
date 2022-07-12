from demoqa_form_test.data.date import Date
from demoqa_form_test.data.student import Student
from demoqa_form_test.model.application_manager import ApplicationManager

def test_form():
    student = Student(first_name='Name',
                      last_name='Surname',
                      email='email@gmail.com',
                      gender=1,
                      mobile_number='8800200060',
                      date_of_birth=Date(day=31, month=1, year=1989),
                      subjects=['Chemistry', 'Maths'],
                      hobbies=[1, 3],
                      picture_path=r'resources\e85.jpg',
                      current_address='some street somewhere over there wherever it would be, 11, 48',
                      state='Uttar Pradesh',
                      city='Merrut'
                      )

    app = ApplicationManager(student)

    app.page.open_form.fill_form.submit_form

    app.result.check_content
























