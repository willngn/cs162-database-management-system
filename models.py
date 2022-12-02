from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, Numeric, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.db')
engine.connect()

Base = declarative_base()

class Office(Base):
    __tablename__ = "office"
    id = Column(Integer, primary_key = True)
    # index on name to optimize searching
    name = Column(Text, index = True)

    def __repr__(self):
        return(f'Office {self.id}, name={self.name}')
    
class Agent(Base):
    __tablename__ = "agent"
    id = Column(Integer, primary_key = True)
    name = Column(Text, index = True)
    email = Column(Text, index = True)

    def __repr__(self):
        return(f'Agent {self.id}, name={self.name}')

class Buyer(Base):
    __tablename__ = "buyer"
    id = Column(Integer, primary_key = True)
    name = Column(Text, index = True)
    email = Column(Text, index = True)

    def __repr__(self):
        return(f'Buyer {self.id}, name={self.name}')

class Seller(Base):
    __tablename__ = "seller"
    id = Column(Integer, primary_key = True)
    name = Column(Text, index = True)
    email = Column(Text, index = True)

    def __repr__(self):
        return(f'Seller {self.id}, name={self.name}')

class House(Base):
    __tablename__ = "house"
    id = Column(Integer, primary_key = True)
    officeID = Column(Integer, ForeignKey(Office.id))
    agentID = Column(Integer, ForeignKey(Agent.id))
    sellerID = Column(Integer, ForeignKey(Seller.id))    
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    price = Column(Numeric(11, 2), nullable=False)
    zipcode = Column(Integer)
    sold = Column(Boolean)

    def __repr__(self):
        return(f'House {self.id}, price={self.price}, zipcode={self.zipcode}, sold={self.sold}')

class Listing(Base):
    __tablename__ = "listing"
    id = Column(Integer, primary_key = True)
    houseID = Column(Integer, ForeignKey(House.id))
    buyerID = Column(Integer, ForeignKey(Buyer.id))
    sellerID = Column(Integer, ForeignKey(Seller.id))
    listingPrice = Column(Integer)
    listingDate = Column(DateTime)

    def __repr__(self):
        return(f'Listing {self.id}, house={self.houseID}, price={self.listingPrice}, date={self.listingDate}')

class Commission(Base):
    __tablename__ = "commission"
    id = Column(Integer, primary_key = True)
    agentID = Column(Integer, ForeignKey(Agent.id))
    listingID = Column(Integer, ForeignKey(Listing.id))
    commission = Column(Integer)

    def __repr__(self):
        return(f'For Listing {self.listingID}, agent {self.agentID} receives commission of {self.commission}')