#!/usr/bin/python3
"""Start link class to table in database"""
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
import sys

Base = declarative_base()


class City(Base):
    """City class"""
    # Link to the MySQL table states
    __tablename__ = 'cities'
    # id column
    id = Column(Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True)
    # name column
    name = Column(String(128), nullable=False)
    # state_id column
    state_id = Column(Integer,
                ForeignKey('states.id'),
                nullable=False)


if __name__ == "__main__":
    # Create an engine that connects to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create the table in the database
    Base.metadata.create_all(engine)
