#!/usr/bin/python3
""" This script lists all states from a database """

import MySQLdb
from sys import argv

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

cursor_object.execute("SELECT * from states")
rows = cursor_object.fetchall()
for row in rows:
    print("{}".format(row))
