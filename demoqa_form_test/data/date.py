from dataclasses import dataclass

from demoqa_form_test.utils import Months


@dataclass()
class Date:
    day: int
    month: int
    year: int

    '''   
    Выше короткая запись этого:
     
    class Date:
        def __init__(self, day: int, month: int, year: int):
            self.day = day
            self.month = month
            self.year = year
    
    '''

    def __str__(self):
        month = Months(self.month).name.title()
        return f'{self.day} {month},{self.year}'
