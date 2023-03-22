#!/usr/bin/python3
""" This script takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
The script takes 4 arguments:
- mysql username,
- mysql password,
- database name,
- state name searched"""


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
    state_name = sys.argv[4].replace('"', '').replace("'","").replace(";","").replace("TABLE", "")
    print(state_name)

    cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
            .format(state_name))

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    conn.close()
