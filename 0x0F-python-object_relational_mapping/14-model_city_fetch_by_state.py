#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa.
Args:
    mysql username, mysql password and database name"""

if __name__ == "__main__":
    from sys import argv
    from urllib.parse import quote_plus
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}"
            .format(argv[1], quote_plus(argv[2]), argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.\
        query(State, City).\
        filter(State.id == City.state_id).\
        order_by(City.id.asc()).\
        all()

    for state, city in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
