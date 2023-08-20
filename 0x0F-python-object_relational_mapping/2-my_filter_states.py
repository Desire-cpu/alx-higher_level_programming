#!/usr/bin/python3

"""
Script that lists all `states` from the database `hbtn_0e_0_usa`.

Arguments:
    takes in four arguments,
    the arguments are strings,
    name searched.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    first = sys.argv[1]
    second = sys.argv[2]
    third = sys.argv[3]

    name_searched = sys.argv[4]

    # By default, it will connect to localhost:3306

    db = MySQLdb.connect(user=first, passwd=second, db=third)
    curs = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}%'".format(name_searched)
    curs.execute(query)
    rows = curs.fetchall()

    for row in rows:
        print(row)
