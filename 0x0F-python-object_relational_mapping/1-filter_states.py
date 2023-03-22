#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
The script takes 3 arguments:
- mysql username
- mysql password
- database name
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8')
    cur = conn.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)
