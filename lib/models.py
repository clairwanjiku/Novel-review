# Import necessary SQLAlchemy modules
from sqlalchemy import create_engine, inspect
from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy database engine
engine = create_engine('sqlite:///novels.db')
inspector = inspect(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create a base class for declarative models
Base = declarative_base()

# Define a many-to-many relationship table between novels and customers
novel_customer = Table(
    'novel_customers',
    Base.metadata,
    Column('novel_id', ForeignKey('novels.id'), primary_key=True),
    Column('customer_id', ForeignKey('customers.id'), primary_key=True),
    extend_existing=True,
)

# Define the Novel class with attributes and relationships
# ...

# ...

class Novel(Base):
    __tablename__ = 'novels'
    
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    price = Column(Integer())
    
    author = Column(String())
    genre = Column(String())
    
    customer = relationship('Customer',secondary=novel_customer, back_populates='novels')
    reviews = relationship('Review', back_populates='novel', cascade='all, delete-orphan')
    

    def __repr__(self):
        return f'novel (id={self.id}, ' + \
            f'name = {self.name}, ' + \
            f'price = {self.price}, ' + \
            f'author = {self.author}, ' + \
            f'genre = {self.genre})'

# ...


class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    
    novels = relationship('Novel',secondary=novel_customer, back_populates='customer')
    reviews = relationship('Review', back_populates='customer', cascade='all, delete-orphan')
    
         
    def __repr__(self):
        return f'Customer (id={self.id}),' +\
            f'name = {self.first_name},' +\
            f'price = {self.last_name})'

# ...



# Define the Review class with attributes and relationships
class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer(), primary_key=True)
    star_rating = Column(Integer())
    
    novel_id = Column(Integer(), ForeignKey('novels.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))
    
    novel = relationship('Novel', back_populates='reviews')
    customer = relationship('Customer', back_populates='reviews')
    
    
    def __repr__(self):
        return f'Review (id={self.id}, ' +\
            f'star rating given = {self.star_rating}, ' +\
            f'novel id ={self.novel_id})'

# Create the database tables based on the defined models
Base.metadata.create_all(engine)