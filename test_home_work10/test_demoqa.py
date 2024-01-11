from data.user import User
from page.registration_page import RegistrationPage


student = User(f_name='Мистер',
               l_name='Твистер',
               email='glavniy@ministr.ru',
               gender='Female',
               mobile='7925002222',
               date_of_birth='18 July,1993',
               subject='Maths',
               hobbie='Reading',
               picture_name='picture.png',
               address='Petrovka 38',
               state='Uttar Pradesh',
               city='Merrut')


def test_fill_form():
    registration = RegistrationPage()
    registration.open_registration_page()
    registration.user_registration(student)
    registration.should_registered_user_with(student)
