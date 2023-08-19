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
    mySql_user = sys.argv[1]
    mySql_password = sys.argv[2]
    mySql_database = sys.argv[3]

    # By default, it will connect to localhost:3306

    db = MySQLdb.connect(user=mySql_user, passwd=mySql_password, db=mySql_database)
    curs = db.cursor()

    curs.execute("SELECT * FROM states ORDER BY id")
    rows = curs.fetchall()

    for row in rows:
        print(row)
