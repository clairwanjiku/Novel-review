import click
from sqlalchemy.orm import Session
from lib.models import Customer, Novel, Review, engine

# Create a global session
session = Session(bind=engine)

@click.group()
def cli():
    """
    CLI for interacting with the Novel Library Database.
    """
    pass

@cli.command()
@click.option('--first-name', prompt='Enter first name', help='First name of the customer.')
@click.option('--last-name', prompt='Enter last name', help='Last name of the customer.')
def create_customer(first_name, last_name):
    """
    Create a new customer.
    """
    new_customer = Customer(first_name=first_name, last_name=last_name)
    session.add(new_customer)
    session.commit()
    click.echo(f"Customer {first_name} {last_name} created successfully!")

@cli.command()
def view_customers():
    """
    View a list of all customers.
    """
    customers = session.query(Customer).all()
    for customer in customers:
        click.echo(f"Customer ID: {customer.id}, Name: {customer.first_name} {customer.last_name}")

@cli.command()
@click.option('--customer-id', prompt='Enter customer ID', type=int, help='ID of the customer to update.')
@click.option('--new-first-name', prompt='Enter new first name', help='New first name for the customer.')
@click.option('--new-last-name', prompt='Enter new last name', help='New last name for the customer.')
def update_customer(customer_id, new_first_name, new_last_name):
    """
    Update customer details.
    """
    customer = session.query(Customer).get(customer_id)
    if customer:
        customer.first_name = new_first_name
        customer.last_name = new_last_name
        session.commit()
        click.echo(f"Customer {customer_id} updated successfully!")
    else:
        click.echo(f"Customer with ID {customer_id} not found.")

@cli.command()
@click.option('--customer-id', prompt='Enter customer ID', type=int, help='ID of the customer to delete.')
def delete_customer(customer_id):
    """
    Delete a customer.
    """
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
        click.echo(f"Customer {customer_id} deleted successfully!")
    else:
        click.echo(f"Customer with ID {customer_id} not found.")

@cli.command()
@click.option('--customer-id', prompt='Enter customer ID', type=int, help='ID of the customer to view reviews.')
def view_customer_reviews(customer_id):
    """
    View all novels a customer has reviewed with name and author.
    """
    customer = session.query(Customer).get(customer_id)
    if customer:
        reviews = session.query(Review).filter_by(customer_id=customer_id).all()
        for review in reviews:
            novel = review.novel
            click.echo(f"Novel ID: {novel.id}, Name: {novel.name}, Author: {novel.author}")
    else:
        click.echo(f"Customer with ID {customer_id} not found.")

@cli.command()
@click.option('--novel-id', prompt='Enter novel ID', type=int, help='ID of the novel to review.')
@click.option('--customer-id', prompt='Enter customer ID', type=int, help='ID of the customer providing the review.')
@click.option('--star-rating', prompt='Enter star rating', type=int, help='Star rating for the review.')
def add_review(novel_id, customer_id, star_rating):
    """
    Add a review to a novel.
    """
    new_review = Review(customer_id=customer_id, novel_id=novel_id, star_rating=star_rating)
    session.add(new_review)
    session.commit()
    click.echo(f"Review added successfully!")

@cli.command()
def view_all_novels():
    """
    View all novels in the library.
    """
    novels = session.query(Novel).all()
    for novel in novels:
        click.echo(f"Novel ID: {novel.id}, Name: {novel.name}, Author: {novel.author}, Genre: {novel.genre}")

@cli.command()
def view_all_reviews():
    """
    View all reviews in the database.
    """
    reviews = session.query(Review).all()
    for review in reviews:
        click.echo(f"Review ID: {review.id}, Novel: {review.novel}, Star Rating: {review.star_rating} by Customer: {review.customer} ")

@cli.command()
@click.option('--review-id', prompt='Enter review ID', type=int, help='ID of the review to update.')
@click.option('--new-star-rating', prompt='Enter new star rating', type=int, help='New star rating for the review.')
def update_review(review_id, new_star_rating):
    """
    Update a review.
    """
    review = session.query(Review).get(review_id)
    if review:
        review.star_rating = new_star_rating
        session.commit()
        click.echo(f"Review {review_id} updated successfully!")
    else:
        click.echo(f"Review with ID {review_id} not found.")

@cli.command()
@click.option('--review-id', prompt='Enter review ID', type=int, help='ID of the review to delete.')
def delete_review(review_id):
    """
    Delete a review.
    """
    review = session.query(Review).get(review_id)
    if review:
        session.delete(review)
        session.commit()
        click.echo(f"Review {review_id} deleted successfully!")
    else:
        click.echo(f"Review with ID {review_id} not found.")

@cli.command()
@click.option('--user-id', prompt='Enter user ID', type=int, help='ID of the user to find.')
def find_user_by_id(user_id):
    """
    Find a user by ID.
    """
    user = session.query(Customer).get(user_id)
    if user:
        click.echo(f"User found - ID: {user.id}, Name: {user.first_name} {user.last_name}")
    else:
        click.echo(f"User with ID {user_id} not found.")

@cli.command()
@click.option('--novel-id', prompt='Enter novel ID', type=int, help='ID of the novel to find.')
def find_novel_by_id(novel_id):
    """
    Find a novel by ID.
    """
    novel = session.query(Novel).get(novel_id)
    if novel:
        click.echo(f"Novel found - ID: {novel.id}, Name: {novel.name}, Author: {novel.author}, Genre: {novel.genre}")
    else:
        click.echo(f"Novel with ID {novel_id} not found.")

@cli.command()
@click.option('--review-id', prompt='Enter review ID', type=int, help='ID of the review to find.')
def find_review_by_id(review_id):
    """
    Find a review by ID.
    """
    review = session.query(Review).get(review_id)
    if review:
        click.echo(f"Review found - ID: {review.id}, Star Rating: {review.star_rating}")
        click.echo(f"Novel: {review.novel.name}, Author: {review.novel.author}")
        click.echo(f"Customer: {review.customer.first_name} {review.customer.last_name}")
    else:
        click.echo(f"Review with ID {review_id} not found.")

# Add other CLI commands...

# Close the session when the CLI program finishes
@cli.command()
def close_session():
    """
    Close the session.
    """
    session.close()
    click.echo("Session closed.")

if __name__ == '__main__':
    cli()
