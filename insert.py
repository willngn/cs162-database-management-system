from models import *
from sqlalchemy.orm import sessionmaker 
import pandas as pd
from sqlalchemy import case
from datetime import datetime

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine) 

Session = sessionmaker(bind=engine)
session = Session()

office_keys = ['id', 'name']
office_info = [
    [0, "LinkedOut"],
    [1, "Uper"],
    [2, "Gugle"],
    [3, "Macrosoft"],
    [4, "Handbook"],
    [5, "Amazin"],
    [6, "Tabledash"],
    [7, "Twitty"],
    [8, "CZI"],
    [9, "Lift"]
]

agent_keys = ['id', 'name', 'email']
agent_info = [
    [0, "Polina", "polina@gmail.com"],
    [1, "Saad", "saad@gmail.com"],
    [2, "Pierre", "pierre@gmail.com"],
    [3, "Chloe", "chloe@gmail.com"],
    [4, "Gabriel", "gabriel@gmail.com"],
    [5, "Woo", "woo@gmail.com"]
]

seller_keys = ['id', 'name', 'email']
seller_info = [
    [0, "Jim", "jim@gmail.com"],
    [1, "John", "john@gmail.com"],
    [2, "Lenny", "lenny@gmail.com"],
    [3, "Nacho", "nacho@gmail.com"],
    [4, "Laura", "laura@gmail.com"],
    [5, "Lui", "lui@gmail.com"],
    [6, "Jan", "jan@gmail.com"],
    [7, "Mara", "mara@gmail.com"]
]

buyer_keys = ['id', 'name', 'email']
buyer_info = [
    [0, "Alina", "alina@gmail.com"],
    [1, "Mako", "mako@gmail.com"],
    [2, "Dilnaz", "dee@gmail.com"],
    [3, "Erela", "erela@gmail.com"],
    [4, "Georgi", "georgi@gmail.com"],
    [5, "Ivanna", "ivanna@gmail.com"],
    [6, "Viktor", "viktor@gmail.com"],
    [7, "Katriel", "katriel@gmail.com"],
    [8, "Karoline", "karo@gmail.com"],
    [9, "Fuong", "fuong@gmail.com"],
    [10, "Tianhui", "tianhui@gmail.com"],
    [11, "Edith", "edith@gmail.com"],
    [12, "Anu", "anu@gmail.com"]
]

house_keys = ['id', 'officeID', 'agentID', 'sellerID', 'bedrooms', 'bathrooms', 'price', 'zipcode', 'sold']
house_info = [
    [0, 3, 2, 2, 2, 2, 120000, 94102, False],
    [1, 2, 3, 3, 1, 1, 75000, 10178, False],
    [2, 4, 4, 1, 3, 1, 150000, 10179, False],
    [3, 5, 5, 6, 4, 2, 180000, 94103, False],
    [4, 1, 2, 5, 5, 5, 210000, 42000, False],
    [5, 0, 3, 6, 2, 2, 125000, 13901, False],
    [6, 8, 5, 7, 3, 3, 160000, 13410, False],
    [7, 9, 0, 7, 1, 1, 90000, 42011, False],
    [8, 2, 0, 2, 2, 1, 100000, 10178, False],
    [9, 6, 1, 3, 2, 1, 110000, 14984, False],
    [10, 4, 1, 4, 4, 3, 175000, 10179, False],
    [11, 1, 2, 1, 3, 1, 80000, 94100, False],
    [12, 0, 5, 0, 4, 4, 250000, 13901, False]
]

for i in range(len(agent_info)):
    # get a temporary holder to store an observation
    holder = agent_info[i]
    # add to the table
    agent = Agent(id = holder[0], name = holder[1], email = holder[2])
    session.add(agent)
session.commit()

for i in range(len(office_info)):
    holder = office_info[i]
    office = Office(id = holder[0], name = holder[1])
    session.add(office)
session.commit()

for i in range(len(seller_info)):
    holder = seller_info[i]
    seller = Seller(id = holder[0], name = holder[1], email = holder[2])
    session.add(seller)
session.commit()

for i in range(len(buyer_info)):
    holder = buyer_info[i]
    buyer = Buyer(id = holder[0], name = holder[1], email = holder[2])
    session.add(buyer)
session.commit()

for i in range(len(house_info)):
    holder = house_info[i]
    house = Listing(id = holder[0], officeID = holder[1], agentID = holder[2], sellerID = holder[3], bedrooms = holder[4], bathrooms = holder[5], price = holder[6], zipcode = holder[7], sold = holder[8])
    session.add(house)
session.commit()
session.close()

print("Agent Table:")
print(pd.read_sql(session.query(Agent).statement, session.bind))
print("---------------------------------------------------------")

print("Office Table:")
print(pd.read_sql(session.query(Office).statement, session.bind))
print("---------------------------------------------------------")

print("Buyer Table:")
print(pd.read_sql(session.query(Buyer).statement, session.bind))
print("---------------------------------------------------------")

print("Seller Table:")
print(pd.read_sql(session.query(Seller).statement, session.bind))
print("---------------------------------------------------------")

print("Listing Table:")
print(pd.read_sql(session.query(Listing).statement, session.bind))
print("---------------------------------------------------------")
Session = sessionmaker(bind=engine)
session = Session()

def transaction(house_id, buyer_id, date):
    """
    This function demonstrates what happens to the database system given a transaction occurs.
    It takes in the house bought, the buyer and the date of transaction

    Expected behaviors:
    - Compute the commission rate for the corresponding agent
    - Update the house status in the House database
    - Add this transaction to the Transaction, Commission database --> Commit
    """

    # Commission rate
    price = session.query(Listing.price).filter(Listing.id == house_id).first()[0]

    # i referenced this thread: https://stackoverflow.com/questions/5430640/sqlalchemy-case-statement-case-if-then-else
    commission_rate = case([(price < 100000, 0.1), 
           (price < 200000, 0.075), 
           (price < 500000, 0.06), 
           (price  < 1000000, 0.05),
           (price  > 1000000, 0.04)])

    # update sold status
    house_sold = session.query(Listing).filter(Listing.id == house_id)
    house_sold.update({Listing.sold: True})
    session.commit()

    # Add to Transaction Database
    seller_id = session.query(Listing.sellerID).filter(Listing.id == house_id).first()[0]
    transactionEntry = Transaction(houseID = house_id, buyerID = buyer_id, sellerID = seller_id, listingPrice = price, listingDate = date)
    session.add(transactionEntry)
    session.commit()

    # Add to Commission Database
    transaction_id = session.query(Transaction.id).filter(Transaction.houseID == house_id).first()[0]
    agent_id = session.query(Listing.agentID).filter(Listing.id == house_id).first()[0]
    commissionEntry = Commission(agentID = agent_id, transactionID = transaction_id, commission = price * commission_rate)
    session.add(commissionEntry)
    session.commit()
    session.close()

# insert fictious data
# reference https://stackoverflow.com/questions/30344237/error-sqlite-datetime-type-only-accepts-python-datetime-and-date-objects-a to debug datetime object
transaction(1, 10, datetime(2022, 12, 1, 10, 10, 10))
transaction(5, 5, datetime(2022, 11, 25, 10, 10, 10))
transaction(11, 3, datetime(2022, 10, 21, 10, 10, 10))
transaction(7, 0, datetime(2022, 9, 12, 10, 10, 10))
transaction(0, 1, datetime(2022, 11, 11, 10, 10, 10))
transaction(2, 8, datetime(2022, 10, 1, 10, 10, 10))
transaction(6, 2, datetime(2022, 12, 10, 10, 10, 10))
transaction(4, 4, datetime(2022, 12, 8, 10, 10, 10))

# verify sold status
print("Listing Table:")
print(pd.read_sql(session.query(Listing).statement, session.bind))
print("---------------------------------------------------------")
# verify commission database
print("Commission Table:")
print(pd.read_sql(session.query(Commission).statement, session.bind))
print("---------------------------------------------------------")
# verify transaction database
print("Transaction Table:")
print(pd.read_sql(session.query(Transaction).statement, session.bind))