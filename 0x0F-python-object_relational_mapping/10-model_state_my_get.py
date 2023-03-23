#!/usr/bin/python3
""" This script prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Args:
    mysql username, mysql password, database name and state name to search"""

if __name__ == "__main__":
    from sys import argv
    from urllib.parse import quote_plus
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], quote_plus(argv[2]), argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = argv[4].replace("'", "").replace('"', '')

    result = session.query(State).filter(State.name == state_name).all()

    if result:
        for r in result:
            print(r.id)
    else:
        print("Not found")

    session.close()
