#!/usr/bin/python3
"""The script deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
Args:
    mysql username, mysql password and database name"""

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

    result = session.query(State).filter(State.name.like('%a%')).all()

    for r in result:
        session.delete(r)

    session.commit()

    session.close()
