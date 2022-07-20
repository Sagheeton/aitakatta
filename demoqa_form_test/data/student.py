from dataclasses import dataclass

from demoqa_form_test.data.date import Date
from demoqa_form_test.data.gender import Gender
from demoqa_form_test.data.hobbies import Hobbies


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    mobile_number: str
    date_of_birth: Date
    subjects: list[str]
    hobbies: list[Hobbies]
    picture_path: str
    current_address: str
    state: str
    city: str

