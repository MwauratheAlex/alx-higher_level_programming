#!/usr/bin/python3
"""This script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
The script should take 4 arguments:
mysql username,
mysql password,
database name and
state name"""


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

    state_name = sys.argv[4].replace("'", "").replace('"', '').replace(" ", "")

    query = "SELECT cities.name FROM cities "
    query += "JOIN states ON states.id=cities.state_id "
    query += f"WHERE states.name LIKE BINARY '{state_name}'"

    cur.execute(query)

    cities = cur.fetchall()

    for i in range(len(cities)):
        print(cities[i][0], end="\n" if i == (len(cities) - 1) else ", ")

    cur.close()
    conn.close()
