#!/usr/bin/python3
""" This script lists all cities from a database """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    user_name, password, database = argv[1], argv[2], argv[3]

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
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """

    cursor_object.execute(query)
    rows = cursor_object.fetchall()
    for row in rows:
        print("{}".format(row))

    cursor_object.close()
    db.close()
