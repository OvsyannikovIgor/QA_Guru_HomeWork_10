from pages.registration_page import RegistrationPage


def test_fill_form():
    registration = RegistrationPage()
    registration.open_registration_page()
    (registration
     .fill_first_name('Мистер')
     .fill_last_name('Твистер')
     .fill_email('glavniy@ministr.ru')
     .choice_gender()
     .fill_user_number('79250022225')
     .fill_date_of_birth(1993, 'July', 18)
     .fill_subjects('Maths')
     .fill_current_address('Petrovka 38')
     .choice_hobies()
     .fill_state('Uttar Pradesh', 'Merrut')
     .upload_picture('picture.png')
     .submit()
     )
    registration.should_registered_user_with()
