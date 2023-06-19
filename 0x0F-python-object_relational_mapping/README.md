Python - Object-Relational Mapping (ORM)

Object-Relational Mapping (ORM) is a technique used in software development to bridge the gap between object-oriented programming languages, such as Python, and relational databases. It allows developers to interact with a database using objects and their relationships, rather than directly writing SQL queries.

Python provides several ORM libraries, with SQLAlchemy being one of the most popular and powerful choices. Here's a short README about Python - Object-Relational Mapping using SQLAlchemy:

1. Installation:
   - Install the SQLAlchemy library using pip:
     ```bash
     pip install sqlalchemy
     ```

2. Establishing a Connection:
   - Create an engine object by specifying the database connection string.
   - The connection string includes details such as the database type, host, username, password, and database name.
   - For example, using MySQL:
     ```python
     from sqlalchemy import create_engine

     engine = create_engine('mysql+mysqlconnector://username:password@localhost/mydatabase')
     ```

3. Defining the Mapped Class:
   - Create a Python class that represents a table in the database.
   - Use SQLAlchemy's `declarative_base()` function to create a base class from which your mapped classes will inherit.
   - Define attributes (columns) of the class using SQLAlchemy's `Column` class.
   - Specify the table name using the `__tablename__` attribute.
   - For example:
     ```python
     from sqlalchemy import Column, Integer, String
     from sqlalchemy.ext.declarative import declarative_base

     Base = declarative_base()

     class MyTable(Base):
         __tablename__ = 'mytable'

         id = Column(Integer, primary_key=True)
         name = Column(String(50))
         age = Column(Integer)
     ```

4. Creating the Table:
   - Use the `Base.metadata.create_all(engine)` method to create the table in the database.
   - This generates the necessary SQL statements based on the class definition.
   - For example:
     ```python
     Base.metadata.create_all(engine)
     ```

5. Working with the Database:
   - Import the necessary modules: `sessionmaker` from `sqlalchemy.orm`.
   - Create a session object using the `sessionmaker` class, passing in the engine.
   - The session object allows you to interact with the database.
   - Example usage:
     ```python
     from sqlalchemy.orm import sessionmaker

     Session = sessionmaker(bind=engine)
     session = Session()

     # Perform database operations using the mapped class and the session object.
     # Examples: querying data, inserting records, updating data, deleting records.

     # Commit changes to the database.
     session.commit()

     # Close the session when done.
     session.close()
     ```

This short README provides a brief overview of Python - Object-Relational Mapping using SQLAlchemy. The process involves establishing a connection, defining a mapped class, creating the table, and working with the database using a session object. Refer to SQLAlchemy's documentation for detailed information and advanced features provided by the  library.
