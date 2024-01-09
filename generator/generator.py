import random
from data.data import Person
from faker import Faker

faker = Faker()

def generated_person():
    yield Person(
        full_name=f"{faker.first_name()} {faker.last_name()} {faker.first_name()}",
        firstname=faker.first_name(),
        lastname=faker.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker.job(),
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )