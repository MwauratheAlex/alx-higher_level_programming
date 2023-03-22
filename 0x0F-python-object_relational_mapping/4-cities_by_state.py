#!/usr/bin/python3
"""This script lists all cities from the database hbtn_0e_4_usa.
The script takes 3 arguments:
mysql username,
mysql password and
database name"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8")

    cur = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name "
    query += "FROM cities JOIN states ON states.id=cities.state_id "
    query += "ORDER BY cities.id ASC"

    cur.execute(query)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()
