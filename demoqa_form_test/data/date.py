from dataclasses import dataclass

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