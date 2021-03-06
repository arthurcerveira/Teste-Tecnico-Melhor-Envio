import os

import sqlalchemy
from sqlalchemy.orm import Session


MYSQL_PASSWORD = os.environ.get('MYSQL_ROOT_PASSWORD')

try:
    engine = sqlalchemy.create_engine(
        f'mysql+mysqlconnector://root:{MYSQL_PASSWORD}@localhost:3306',
        # echo=True   # Setting echo as True prints the database logs
        )
    session = Session(engine)

    with open("../../database-schema/ddl.sql") as ddl:
        session.execute(ddl.read())
except:
    print("Database is not initialized.")
    print("Wait a minute and try again.")
    exit(1)

print("Database was setup correctly.")
