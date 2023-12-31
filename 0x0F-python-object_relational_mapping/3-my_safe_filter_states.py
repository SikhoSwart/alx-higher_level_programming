#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states table
where name matches the argument
But this time write one that is safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (argv[4],))
    rows = cur.fetchall()
    for r in rows:
        print(r)
    cur.close()
    db.close()
