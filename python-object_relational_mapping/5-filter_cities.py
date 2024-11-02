#!/usr/bin/python3

"""
Create a script that lists all the cities of a state given as argument,
using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    List all cities in the cities table of hbtn_0e_4_usa where the state name
    matches the argument.

    Usage:
        ./4-cities_by_state.py
        <mysql username>
        <mysql password>
        <database name>
        <state name>

    Arguments:
        sys.argv[1]: The MySQL username
        sys.argv[2]: The MySQL password
        sys.argv[3]: The MySQL database name
        sys.argv[4]: The state name to match

    Returns:
        The cities in the database with a state name that matches the argument.
    """

    # Get the arguments from the command line
    mysql_un = sys.argv[1]
    mysql_pwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
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
    # Create a query string
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    # Execute the query
    cursor.execute(query, (state_name,))
    # Fetch all the rows in a list of lists
    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))
    # Close the cursor and database
    cursor.close()
    db.close()
