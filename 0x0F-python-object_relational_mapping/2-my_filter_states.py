#!/usr/bin/python3
""" This script takes an argument and displays all values
    in the states table where name matches with argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./2-my_filter_states.py root"
              "root hbtn_0e_0_usa 'state_name'")
        exit(1)

    user_name, password, database, match = argv[1], argv[2], argv[3], argv[4]

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
    SELECT * from states
    WHERE name = '{}'
    ORDER BY states.id ASC
    """.format(match)

    cursor_object.execute(query)
    rows = cursor_object.fetchall()
    for row in rows:
        print("{}".format(row))

    cursor_object.close()
    db.close()
