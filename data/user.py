import dataclasses


@dataclasses.dataclass
class User:
    f_name: str
    l_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: str
    subject: str
    hobbie: str
    picture_name: str
    address: str
    state: str
    city: str
