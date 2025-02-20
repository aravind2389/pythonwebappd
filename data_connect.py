import secrets
from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from sqlalchemy import create_engine


# initialize Cloud SQL Connector
connector = Connector()

# SQLAlchemy database connection creator function
def getconn():
    conn = connector.connect(
        "demoproject-312207:us-central1:testmysql", # Cloud SQL Instance Connection Name
        "pymysql",
        user=secrets.user_name,
        password=secrets.password,
        db=secrets.db_name,
        ip_type=IPTypes.PUBLIC # IPTypes.PRIVATE for private IP
    )
    return conn

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=getconn,
)

with pool.connect() as db_conn:
    # query database and fetch results
    results = db_conn.execute(sqlalchemy.text("SELECT * FROM Persons LIMIT 10;")).fetchall()

    # show results
    for row in results:
        print(row[2:6])

db_conn.close()