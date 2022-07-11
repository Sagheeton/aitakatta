from selene.support.shared.jquery_style import s


class StudentRegistrationPage:
    def set_first_name(self, value):
        s('#firstName').type(value)
        return self

    def set_last_name(self, value):
        s('#lastName').type(value)
        return self

    def set_email(self, value):
        s('#userEmail').type(value)
        return self
