from demoqa_form_test.data.date import Date
from demoqa_form_test.data.gender import Gender
from demoqa_form_test.data.hobbies import Hobbies
from demoqa_form_test.data.student import Student
from demoqa_form_test.model.application_manager import ApplicationManager

def test_form():
    student = Student(first_name='Shapath',
                      last_name='Bharadwaj',
                      email='email@gmail.com',
                      gender=Gender.MALE,
                      mobile_number='8800200060',
                      date_of_birth=Date(day=31, month=1, year=1989),
                      subjects=['Chemistry', 'Maths'],
                      hobbies=[Hobbies.SPORTS, Hobbies.MUSIC],
                      picture_path=r'resources\e85.jpg',
                      current_address='MJPRU Entrance Rd, M.J.P Rohilkahand University',
                      state='Uttar Pradesh',
                      city='Merrut'
                      )

    app = ApplicationManager(student)

    app.page.open_form.fill_form.submit_form

    app.result.check_content
























