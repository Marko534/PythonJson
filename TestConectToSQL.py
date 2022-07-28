from sqlalchemy import create_engine, Column, Integer, String, select, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
import GenerateSQLTables as DB
import json

engine = create_engine('mssql://@MARKO-ILIOSKI/Test?driver=SQL Server Native Client 11.0', echo=True, future=True)
f = open('Json.json')
Json = json.load(f)

session = Session(engine)


for row in Json:
    for Topping in row['batters']['batter']:
        print (Topping['id'])





