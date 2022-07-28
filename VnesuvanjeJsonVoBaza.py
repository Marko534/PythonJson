from sqlalchemy import create_engine, Column, Integer, String, select, ForeignKey
from sqlalchemy.orm import declarative_base, Session, relationship
import GenerateSQLTables as DB
import json

f = open('Json.json')
Json = json.load(f)

engine = create_engine('mssql://@MARKO-ILIOSKI/Test?driver=SQL Server Native Client 11.0', echo=True, future=True)

session = Session(engine)

for RowJson in Json:
    NameList = session.query(DB.Name.name)
    IsInDataBase = False
    for RowDataBase in NameList:
        # PRASHAJ dali povde mozi na poubav nacin da bidi oti mislam mozi
        if RowDataBase.name == RowJson['name']:
            IsInDataBase = True
            break
    if not IsInDataBase:
        session.add(DB.Name(name=RowJson['name']))

session.commit()