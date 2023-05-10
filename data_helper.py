import random
import pandas as pd

from faker import Faker
from bson import ObjectId


def generate_users(n_rows=25):
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


def generate_states(num_rows=50):
    states = ["Ohio", "Michigan", "Alabama", "Texas"]
    state_abbrevs = ["OH", "MI", "AL", "TX"]
    state_data = []

    for i in range(num_rows):
        state = random.choice(states)
        state_abbrev = state_abbrevs[states.index(state)]
        state_data.append((ObjectId(), state_abbrev))
        state_data.append((ObjectId(), state))

    df = pd.DataFrame(state_data, columns=["id", "state"])
    return df.sample(frac=1).reset_index(drop=True)


def generate_gender(n_row=100):
    genders = ["Man", "Woman", "DND"]
    data = {
        "gender": [
            random.choice(genders).lower()
            if random.randint(0, 1) == 0
            else random.choice(genders).upper()
            for _ in range(n_row)
        ]
    }
    return pd.DataFrame(data)


def generate_users_missing(n_row=25):
    data = {
        "ID": [
            random.randint(1, 100) if random.randint(0, 3) != 0 else None
            for _ in range(n_row)
        ],
        "name": [
            "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=5))
            if random.randint(0, 3) != 0
            else None
            for _ in range(n_row)
        ],
        "date_of_birth": [
            f"{random.randint(1950, 2023)}-{random.randint(1, 12):02d}-"
            f"{random.randint(1, 28):02d}"
            if random.randint(0, 3) != 0
            else None
            for _ in range(n_row)
        ],
        "current_country": [
            random.choice(["USA", "Canada", "Mexico"])
            if random.randint(0, 3) != 0
            else None
            for _ in range(n_row)
        ],
    }
    return pd.DataFrame(data)


def generate_age_missing(n_row=25):
    data = {
        "age": [
            random.randint(18, 80) if random.randint(0, 3) != 0 else None
            for _ in range(n_row)
        ]
    }
    return pd.DataFrame(data)
