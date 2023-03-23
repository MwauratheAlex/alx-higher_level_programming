#!/usr/bin/python3
"""The script lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
Args:
    mysql username, mysql password and database name"""


if __name__ == "__main__":
    from sys import argv
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from urllib.parse import quote_plus
    from sqlalchemy import (create_engine)

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], quote_plus(argv[2]), argv[3]),
            pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id.asc()).all()

    for r in result:
        print(f"{r.id}: {r.name}")
