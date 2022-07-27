import sqlalchemy
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

# ConnectionString = 'mssql+pyodbc:// C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\'

engine = create_engine('mssql+pyodbc://MARKO-ILIOSKI/test.mdf', echo=True, future=True)
Base = declarative_base()


class Batter(Base):
    __tablename__ = "Batter"
    BatterId = Column(Integer, primary_key=True)
    Type = Column(String)
    listOfProducts = relationship("ListOfProducts", back_populates="batter")

    def __repr__(self):
        return f"Batter(id={self.BatterId!r}, TypeOfBatter={self.Type!r})"


class Topping(Base):
    __tablename__ = "Topping"
    ToppingId = Column(Integer, primary_key=True)
    Type = Column(String)
    listOfProducts = relationship("ListOfProducts", back_populates="topping")

    def __repr__(self):
        return f"Topping(id={self.ToppingId!r}, TypeOfBatter={self.Type!r})"


class TypeOf(Base):
    __tablename__ = "TypeOf"
    TypeOfId = Column(Integer, primary_key=True)
    Type = Column(String)
    listOfProducts = relationship("ListOfProducts", back_populates="typeof")

    def __repr__(self):
        return f"TypeOf(id={self.TypeOfId!r}, TypeOfBatter={self.Type!r})"


class Name(Base):
    __tablename__ = "Name"
    NameId = Column(Integer, primary_key=True)
    name = Column(String)
    listOfProducts = relationship("ListOfProducts", back_populates="name")

    def __repr__(self):
        return f"Name(id={self.NameId!r}, name={self.name!r})"


class ListOfProducts(Base):
    __tablename__ = 'ListOfProducts'
    barcode = Column(Integer, primary_key=True)
    typeId = Column(Integer, ForeignKey('TypeOf.TypeOfId'))
    nameid = Column(Integer, ForeignKey('Name.NameId'))
    ppu = Column(Integer)
    batterid = Column(Integer, ForeignKey('Batter.BatterId'))
    toppingid = Column(Integer, ForeignKey('Topping.ToppingId'))

    typeof = relationship("TypeOf", back_populates="listOfProducts")
    name = relationship("Name", back_populates="listOfProducts")
    batter = relationship("Batter", back_populates="listOfProducts")
    topping = relationship('Topping', back_populates='listOfProducts')

    def __repr__(self):
        return f"ListOfProducts(barcode={self.barcode!r}, typeId={self.typeId!r}, nameid={self.nameid!r}, ppu={self.ppu!r}, batterid={self.batterid!r}, topping={self.topping!r})"


Base.metadata.create_all(engine)

