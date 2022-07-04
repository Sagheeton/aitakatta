from selene.core import command
from selene.support.shared.jquery_style import s
from selenium.webdriver import Keys

'''
Не вижу смысла передавать сюда элементс самого дейтпикера, так как с ним придется передавать еще три класса
Если айди изменится, можно предположить, что и классы изменятся, так что передавать будем только дату
'''


def choose_by_clicking(day: int, month: int, year: int):
    s('#dateOfBirthInput').click()
    s('[class*="month-select"]').click().element(f'[value="{month}"]').click()
    s('[class*="year-select"]').click().element(f'[value="{year}"]').click()
    s(f'[class*="datepicker__day--0{day}"]').click()

#
# def choose_by_typing():
#   impossible
