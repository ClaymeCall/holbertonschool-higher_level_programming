#!/usr/bin/python3

"""
Create a script that lists all State objects that contain the letter a
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Create a script that lists all State objects that contain the letter a
    from the database hbtn_0e_6_usa

    Usage: ./9-model_state_filter_a.py
        <mysql username>
        <mysql password>
        <database name>
        <state name>

    Arguments:
        mysql_username (str): MySQL username
        mysql_password (str): MySQL password
        database_name (str): MySQL database name
        state_name (str): The state name to fetch

    Returns:
        The id of the state with the name passed as argument
        "Not found" if the state is not found
    """
    # Get the arguments from the command line
    mysql_username, mysql_password, \
        database_name, state_name = sys.argv[1:5]
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name))
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    # Query the database
    state = session.query(State).filter(
        State.name == state_name).first()
    # Print the result
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    # Close the session
    session.close()
