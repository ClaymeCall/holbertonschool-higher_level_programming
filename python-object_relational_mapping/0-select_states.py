#!/usr/bin/python3

"""
Create a connection to the database and retrieve all
states sorted by id from the database specified in the
command line.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Retrieve all states sorted by id from the database
    specified in the command line.

    Usage:
        ./0-select_states.py
        <mysql username>
        <mysql password>
        <database name>

    Arguments:
        sys.argv[1]: The MySQL username
        sys.argv[2]: The MySQL password
        sys.argv[3]: The MySQL database name

    Returns:
        The states in the database sorted by id
    """
    # Get the arguments from the command line
    mysql_un = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    # Connect to the database
    db = MySQLdb.connect(
        # MySQL host
        host="localhost",
        # The port number to connect to MySQL
        port=3306,
        # The user name specified in the command line
        user=mysql_un,
        # The password specified in the command line
        passwd=mysql_pwd,
        # The database name specified in the command line
        db=db_name
    )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    # Fetch all the rows in a list of lists
    states = cursor.fetchall()
    # Iterate over the rows to print the states
    for state in states:
        # Print the state
        print(state)
    # Close the cursor and database
    cursor.close()
    db.close()
