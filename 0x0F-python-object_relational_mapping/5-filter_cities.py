#!/usr/bin/python3
""" This script takes in the name of a state as argument and
    lists all cities of that state
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    user_name, password, database, state = argv[1], argv[2], argv[3], argv[4]

    # establish a connection to the database through the MySQLdb module
    db = MySQLdb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=database,
        port=3306
    )

    # create a working environment using the cursor object
    # to perform operations on the database
    cursor_object = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    WHERE cities.state_id = (
        SELECT states.id
        FROM states
        WHERE states.name = %s
    )
    ORDER BY cities.id ASC
    """

    cursor_object.execute(query, (state, ))
    rows = cursor_object.fetchall()
    city_names = [row[0] for row in rows]

    city_name_str = ", ".join(city_names)
    print(city_name_str)

    cursor_object.close()
    db.close()
