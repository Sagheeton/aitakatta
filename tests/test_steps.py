import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_with_dynamic_steps():
    with allure.step('Открываем главную страницу гитхаба'):
        browser.open('https://github.com')

    with allure.step('Ищем репозиторий'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Нажимаем на вкладку issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличия issue с номером 76'):
        s(by.partial_text('#76')).should(be.visible)


def test_github_with_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number(76)

@allure.step('Открываем главную страницу гитхаба')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Нажимаем на вкладку issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличия issue с номером {value}')
def should_see_issue_with_number(value):
    s(by.partial_text(f'#{value}')).should(be.visible)
