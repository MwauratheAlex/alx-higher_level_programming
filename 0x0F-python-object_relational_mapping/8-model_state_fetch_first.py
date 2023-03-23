#!/usr/bin/python3
"""The script prints the first State object from the database hbtn_0e_6_usa.
Args:
    mysql username, mysql password and database name"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from urllib.parse import quote_plus

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], quote_plus(argv[2]), argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id.asc()).first()

    if result is None:
        print()
    else:
        print(f"{result.id}: {result.name}")
