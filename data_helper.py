import pandas as pd


from faker import Faker
from bson import ObjectId


def generate_fake_data(n_rows=25):
    fake = Faker()
    data = []
    for i in range(n_rows):
        row = [
            ObjectId(),
            fake.name(),
            fake.random_int(min=18, max=65),
            fake.date_of_birth(minimum_age=18, maximum_age=65),
            fake.country(),
        ]
        data.append(row)
    df = pd.DataFrame(
        data, columns=["ID", "name", "AgE", "dateOfBirth", "current_COUNTRY"]
    )
    return df
