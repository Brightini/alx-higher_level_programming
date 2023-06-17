#!/usr/bin/python3
""" This script takes an argument and displays all values
    in the states table where name matches with argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

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

    cursor_object.execute("SELECT * from states WHERE name = %s", (match,))
    rows = cursor_object.fetchall()
    for row in rows:
        print("{}".format(row))
