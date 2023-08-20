#!/usr/bin/python3

"""
Script that lists all `states` from the database `hbtn_0e_0_usa`.

Arguments:
    takes in three arguments,
    the arguments are strings,
"""

import sys
import MySQLdb

if __name__ == "__main__":
    first = sys.argv[1]
    second = sys.argv[2]
    third = sys.argv[3]

    # By default, it will connect to localhost:3306

    db = MySQLdb.connect(user=first, passwd=second, db=third)
    curs = db.cursor()

    curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ")
    rows = curs.fetchall()

    for row in rows:
        print(row)
