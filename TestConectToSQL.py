from sqlalchemy import create_engine, Column, Integer, String, select, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
import GenerateSQLTables as DB

engine = create_engine('mssql://@MARKO-ILIOSKI/Test?driver=SQL Server Native Client 11.0', echo=True, future=True)
Base = declarative_base()


DB.Name

session = Session(engine)
session.add(DB.Name(name="Sofija"))
session.add(DB.Name(name="Nadza"))
session.add(DB.Name(name="Pece"))
session.commit()

for row in session.execute(select(DB.Name)):
    print (row)





