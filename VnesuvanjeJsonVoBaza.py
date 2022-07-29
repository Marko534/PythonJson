from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import GenerateSQLTables as DB
import json

f = open('Json.json')
Json = json.load(f)

engine = create_engine(
    'mssql://@MARKO-ILIOSKI/Doughnuts?driver=SQL Server Native Client 11.0', echo=True, future=True)

session = Session(engine)

"""
Generira tabeli za podatoci so se poftoruva i moza 
da se povrza so relacija za na glavna tabela
"""
for RowJson in Json:
# Za dodavanje na NAME
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
    for RowTopping in RowJson['topping']:
        NameList = session.query(DB.Topping.Id)
        IsInDataBase = False
        for RowDataBase in NameList:
            if RowDataBase.Id == int(RowTopping['id']):
                IsInDataBase = True
                break
        if not IsInDataBase:
            session.add(DB.Topping(
                Id=RowTopping['id'], Type=RowTopping['type']))

# Za BATTERS
    for RowBatter in RowJson['batters']['batter']:
        NameList = session.query(DB.Batter.Id)
        IsInDataBase = False
        for RowDataBase in NameList:
            if RowDataBase.Id == int(RowBatter['id']):
                IsInDataBase = True
                break
        if not IsInDataBase:
            session.add(DB.Batter(Id=RowBatter['id'], Type=RowBatter['type']))
            
"""
Generira glavna tabela so refrences 
do 4rite ostanati
"""
for RowJson in Json:
    for RowBatter in RowJson['batters']['batter']:
        for RowTopping in RowJson['topping']:
            session.add(DB.ListOfProducts(
                typeId = session.query(DB.TypeOf.TypeOfId).filter(DB.TypeOf.Type ==RowJson['type']).one().TypeOfId,
                nameid = session.query(DB.Name.NameId).filter(DB.Name.name == RowJson['name']).one().NameId,
                ppu = int (RowJson['ppu']),
                batterid = session.query(DB.Batter.BatterId).filter(DB.Batter.Id == int(RowBatter['id'])).one().BatterId,
                toppingid = session.query(DB.Topping.ToppingId).filter(DB.Topping.Id == int(RowTopping['id'])).one().ToppingId
                ))

    # typeId = Column(Integer, ForeignKey('TypeOf.TypeOfId'))
    # nameid = Column(Integer, ForeignKey('Name.NameId'))
    # ppu = Column(Integer)
    # batterid = Column(Integer, ForeignKey('Batter.BatterId'))
    # toppingid = Column(Integer, ForeignKey('Topping.ToppingId'))


session.commit()
