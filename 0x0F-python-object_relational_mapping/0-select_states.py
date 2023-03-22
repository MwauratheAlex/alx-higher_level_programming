#!/usr/bin/python3
""" This module contains a script that that lists
all states from the database hbtn_0e_0_usa.
The script should take 3 arguments:
 - mysql username
 - mysql password
 - database name
 """


if __name__ == '__main__':
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8')

    cur = conn.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
