from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, Numeric, DateTime, Boolean, PrimaryKeyConstraint
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

class Listing(Base):
    __tablename__ = "listing"
    # a house - a listing, so the id here can also be interpreted as houseID
    id = Column(Integer, primary_key = True)
    officeID = Column(Integer, ForeignKey(Office.id))
    agentID = Column(Integer, ForeignKey(Agent.id))
    sellerID = Column(Integer, ForeignKey(Seller.id))    
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    zipcode = Column(Integer)
    sold = Column(Boolean)

    def __repr__(self):
        return(f'House {self.id}, price={self.price}, zipcode={self.zipcode}, sold={self.sold}')

class Transaction(Base):
    __tablename__ = "listing"
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key = True, autoincrement=True)
    houseID = Column(Integer, ForeignKey(Listing.id))
    buyerID = Column(Integer, ForeignKey(Buyer.id))
    sellerID = Column(Integer, ForeignKey(Seller.id))
    listingPrice = Column(Integer)
    listingDate = Column(DateTime)

    def __repr__(self):
        return(f'Listing {self.id}, house={self.houseID}, price={self.listingPrice}, date={self.listingDate}')

class Commission(Base):
    __tablename__ = "commission"
    __table_args__ = {'extend_existing': True} 
    id = Column(Integer, primary_key = True, autoincrement=True)
    agentID = Column(Integer, ForeignKey(Agent.id))
    transactionID = Column(Integer, ForeignKey(Transaction.id))
    commission = Column(Integer)

    def __repr__(self):
        return(f'For Listing {self.transactionID}, agent {self.agentID} receives commission of {self.commission}')