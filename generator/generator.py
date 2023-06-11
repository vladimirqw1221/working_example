
from faker import Faker

from data.data import Pesron

faker_ru = Faker('ru_RU')




def generator():
    yield Pesron(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        zip_cade=faker_ru.postcode()
    )