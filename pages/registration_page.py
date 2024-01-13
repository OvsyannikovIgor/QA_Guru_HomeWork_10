from selene import browser, have

import resource


# GENDER_1 = '#gender-radio-1'
# GENDER_2 = '#gender-radio-2'
# GENDER_3 = '#gender-radio-3'
# HOBBIES_1 = '[for="hobbies-checkbox-1"]'
# HOBBIES_2 = '[for="hobbies-checkbox-2"]'
# HOBBIES_3 = '[for="hobbies-checkbox-2"]'


class RegistrationPage():
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.gender = browser.element('#gender-radio-2')
        self.email = browser.element('#userEmail')
        self.mobile = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.subject = browser.element('#subjectsInput')
        self.adress = browser.element('#currentAddress')
        self.hobies = browser.element('[for="hobbies-checkbox-2"]')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.picture = browser.element('#uploadPicture')
        self.submit = browser.element('#submit')
        self.completed_registration_form = browser.all(' table > tbody > tr').all('td:nth-child(2)')
        pass

    def open_registration_page(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def choice_gender(self):
        self.gender.double_click()
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def fill_user_number(self, value):
        self.mobile.type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        self.date_of_birth.click()
        self.month_of_birth.type(month)
        self.year_of_birth.type(year)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()
        return self

    def fill_subjects(self, value):
        self.subject.type(value).press_enter()
        return self

    def fill_current_address(self, value):
        self.adress.type(value)
        return self

    def choice_hobies(self):
        self.hobies.click()
        return self

    def fill_state(self, state, city):
        self.state.type(state).press_enter()
        self.city.type(city).press_enter()
        return self

    def upload_picture(self, value):
        return self.picture.set_value(resource.path(value))

    def should_registered_user_with(self):
        self.completed_registration_form.should(
            have.exact_texts('Мистер Твистер',
                             'glavniy@ministr.ru',
                             'Female', '7925002222',
                             '18 July,1993',
                             'Maths',
                             'Reading',
                             'picture.png',
                             'Petrovka 38',
                             'Uttar Pradesh Merrut')
        )

    def submit_btn(self):
        return self.submit.press_enter()
