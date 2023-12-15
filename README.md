## Novel Library CLI
This CLI application allows users to interact with a novel library database, manage customers, novels, reviews, and perform various operations through a command-line interface.

### Utilize an algorithm from the Data Structures and Algorithms module within the CLI functionality.
Usage
CLI Commands
create_customer: Create a new customer.
view_customers: View a list of all customers.
update_customer: Update customer details.
delete_customer: Delete a customer.
add_review: Add a review to a novel.
view_customer_reviews: View all novels a customer has reviewed.
view_all_novels: View all novels in the library.
view_all_reviews: View all reviews in the database.
update_review: Update a review.
delete_review: Delete a review.
find_user_by_id: Find a user by ID.
find_novel_by_id: Find a novel by ID.
find_review_by_id: Find a review by ID.
close_session: Close the session.
## Example Commands
To PERFORM AN EXECUTION:  python3 main.py <CLI COMMAND>




### HOW IT WORKS ####
For a customer to review  a book they have to be have added to the system and a book needs to be in the data as well. for a customer/reader to review a book they need to know the id of the novel and their id as well.

###### Learning Goals #######
Configure environments with project-specific parameters using Pipenv.
Import and use external libraries.
Use SQLAlchemy ORM and Alembic to create a database schema and update it as you continue to build your CLI.
Implement SQLAlchemy ORM to establish one-to-one, one-to-many, and many-to-many relationships between tables.
Incorporate algorithms from Data Structures and Algorithms (DSA) module.
Apply best practices in CLI design and maintain a well-structured codebase.
Installation and Setup

### Clone the repository.
Install dependencies using Pipenv:
#pipenv install

Activate the virtual environment:
#pipenv shell
Set up the database:
bash

# Run migrations using Alembic
alembic upgrade head
Features
Create, Read, Update, Delete (CRUD) Operations

Manage customers: create, view, update, delete customer information.
View all novels in the library.
View and update reviews provided by customers.
Search for users, novels, or reviews by their respective IDs.
Algorithm Implementation




#novel-cli create_customer --first-name John --last-name Doe

To view all novels:
#novel-cli view_all_novels
##### Project Structure
/cli: Contains the CLI functionality.
/models: Includes the database models using SQLAlchemy ORM.
/scripts: Houses additional scripts or utilities.
/tests: Contains unit tests for the application.
Contributing
We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.


Project Structure
Files Provided
cli.py:

Functionality: Contains the CLI commands and their implementations using Click or Fire.
Snippet:
python
Copy code
import click

@click.command()
def view_all_novels():
    # Implementation to view all novels
    pass

@click.command()
def create_customer(first_name, last_name):
    # Implementation to create a customer
    pass
Example Usage:
bash

$ novel-cli view_all_novels
$ novel-cli create_customer --first-name John --last-name Doe
models.py:

###### Functionality: Contains SQLAlchemy ORM models defining database tables and their relationships.#####
Snippet:
python
Copy code
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    # Relationships
    reviews = relationship('Review', back_populates='customer')

class Novel(Base):
    __tablename__ = 'novels'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    # Relationships
    reviews = relationship('Review', back_populates='novel') 

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    # Relationships
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship('Customer', back_populates='reviews')
    novel_id = Column(Integer, ForeignKey('novels.id'))
    novel = relationship('Novel', back_populates='reviews')
Example Usage:
python
Copy code
# Create a new customer
new_customer = Customer(first_name='John', last_name='Doe')
session.add(new_customer)
session.commit()
database_setup.py:

Functionality: Contains the database setup and configuration using SQLAlchemy and Alembic for migrations.
Snippet:
python
Copy code
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///novel_library.db')
Session = sessionmaker(bind=engine)
session = Session()
Example Usage:
python
Copy code
# Set up the database
from database_setup import session
from models import Base
Base.metadata.create_all(engine)
utils.py (hypothetical):

Functionality: Contains utility functions or helper methods used across the project.
Snippet:
python
Copy code
def find_user_by_id(user_id):
    # Implementation to find a user by ID
    pass

def find_novel_by_id(novel_id):
    # Implementation to find a novel by ID
    pass
Example Usage:
python
Copy code
# Find a user by ID
user = find_user_by_id(1)

aurthor
clair, Daniel, Sandra and Ian
liscence under TMI
