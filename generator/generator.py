from data.data import Person
from faker import Faker

faker = Faker()

def generated_person():
    yield Person(
        full_name=f"{faker.first_name()} {faker.last_name()} {faker.first_name()}",
        email=faker.email(),
        current_address=faker.address(),
        permanent_address=faker.address()
    )