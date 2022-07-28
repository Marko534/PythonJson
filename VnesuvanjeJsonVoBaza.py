from sqlalchemy import create_engine
from sqlalchemy.orm import  Session
import GenerateSQLTables as DB
import json

f = open('Json.json')
Json = json.load(f)

engine = create_engine('mssql://@MARKO-ILIOSKI/Test?driver=SQL Server Native Client 11.0', echo=True, future=True)

session = Session(engine)

# Za dodavanje na NAME
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

# Za dodavanje na TYPEOF
for RowJson in Json:
    NameList = session.query(DB.TypeOf.Type)
    IsInDataBase = False
    for RowDataBase in NameList:
        # PRASHAJ dali povde mozi na poubav nacin da bidi oti mislam mozi
        if RowDataBase.Type == RowJson['type']:
            IsInDataBase = True
            break
    if not IsInDataBase:
        session.add(DB.TypeOf(Type=RowJson['type']))
        
# Za TOPPINGS
for RowJson in Json:
    for RowTopping in RowJson['topping']:
        NameList = session.query(DB.Topping.Id)
        IsInDataBase = False
        for RowDataBase in NameList:
            if RowDataBase.Id == int (RowTopping['id']):
                IsInDataBase = True
                break
        if not IsInDataBase:
            session.add(DB.Topping(Id=RowTopping['id'], Type=RowTopping['type']))
# Za BATTERS            
for RowJson in Json:
    for RowBatter in RowJson['batters']['batter']:
        NameList = session.query(DB.Batter.Id)
        IsInDataBase = False
        for RowDataBase in NameList:
            if RowDataBase.Id == int (RowBatter['id']):
                IsInDataBase = True
                break
        if not IsInDataBase:
            session.add(DB.Batter(Id=RowBatter['id'], Type=RowBatter['type']))

# Za
session.commit()