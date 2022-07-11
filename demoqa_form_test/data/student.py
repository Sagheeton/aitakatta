from dataclasses import dataclass

from demoqa_form_test.data.date import Date


@dataclass
class Student:
    first_name: str
    last_name: str
    email: str
    gender: int #temoporarily, later change to enum
    mobile_number: str
    date_of_birth: Date
    subjects: list[str]
    hobbies: list[int] #also would like to change it to list of enums
    picture_path: str
    current_address: str
    state: str
    city: str
