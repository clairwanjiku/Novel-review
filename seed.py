from faker import Faker
from lib.models import Novel, Customer, Review, engine
from sqlalchemy.orm import Session
import random
session = Session(bind=engine)
# Create Faker instance
fake = Faker()

# Seed the database with fake data
for _ in range(10):  # Adjust the range to the desired number of entries
    # Create Novel entries
    novel = Novel(
        name=fake.catch_phrase(),
        price=random.randint(10, 100),
        author=fake.name(),
        genre=fake.word()
    )
    session.add(novel)

    # Create Customer entries
    customer = Customer(
        first_name=fake.first_name(),
        last_name=fake.last_name()
    )
    session.add(customer)

    # Create Review entries
    review = Review(
        star_rating=random.randint(1, 5),
        novel=novel,
        customer=customer
    )
    session.add(review)

# Commit the changes to the database
session.commit()
