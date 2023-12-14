
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Create an SQLite database in memory for testing
engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)

# Creating a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# sample data
restaurant1 = Restaurant(name="Restaurant A", price=2)
restaurant2 = Restaurant(name="Restaurant B", price=3)
customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Doe")
review1 = Review(rating=5, customer=customer1, restaurant=restaurant1)
review2 = Review(rating=4, customer=customer2, restaurant=restaurant1)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()

# Testing relationships & methods
print("Reviews for Restaurant A:")
for review in restaurant1.reviews:
    print(f"- {review.customer.full_name()}: {review.rating} stars")

print("\nCustomers who reviewed Restaurant A:")
for customer in restaurant1.customers:
    print(f"- {customer.full_name()}")

print("\nReviews by John Doe:")
for review in customer1.reviews:
    print(f"- {review.restaurant.name}: {review.rating} stars")

print("\nRestaurants reviewed by John Doe:")
for restaurant in customer1.restaurants:
    print(f"- {restaurant.name}")
