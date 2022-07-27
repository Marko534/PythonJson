import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import  Column, Integer, String, select
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)
    addresses = relationship("Address", back_populates="user")
    def __repr__(self):
       return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'))
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
    
Base.metadata.create_all(engine)

session = Session(engine)
session.add(User(name="squidward", fullname="Squidward Tentacles"))
session.add(User(name="sandy", fullname="Sandy Cheeks"))
session.add(User(name="ehkrabs", fullname="Eugene H. Krabs"))

session.commit()

for row in session.execute(select(User)):
    print (row)


# session.close()
