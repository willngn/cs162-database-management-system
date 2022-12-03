from models import *
from insert import Transaction
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text, func
import pandas as pd

Session = sessionmaker(bind=engine)
session = Session()

# DECEMBER
# referece: https://www.geeksforgeeks.org/how-to-execute-raw-sql-in-sqlalchemy/
print("Question 1: top 5 offices with the most sales for that month.")
sql1 = text("SELECT name, Count(officeID) FROM (SELECT * FROM Office Join Listing ON Office.id == Listing.officeID WHERE sold == True) GROUP BY officeID ORDER BY Count(officeID) DESC LIMIT 5")
results = engine.execute(sql1)

for record in results:
    print("\n", record)

print("Question 2: top 5 estate agents who have sold the most for the month")
sql2 = text("SELECT Agent.name, Agent.email, COUNT(Listing.agentID) FROM Agent JOIN Listing ON Agent.id == Listing.agentID WHERE Listing.sold == TRUE GROUP BY Listing.agentID ORDER BY Count(Listing.agentID) DESC LIMIT 5")
results = engine.execute(sql2)

for record in results:
    print("\n", record)

# TESTING: it's true because only Saad are the only agent who has not sold any houses yet

print("Question 3: the commission that each estate agent must receive")
# we already have a separate Commission table
sql3 = text("SELECT name, email, SUM(commission) FROM (SELECT * FROM Agent Join Commission ON Agent.id == Commission.agentID) GROUP BY agentID ORDER BY SUM(Commission) DESC")
results = engine.execute(sql3)

for record in results:
    print("\n", record)

# TESTING: makes sense with the above result

print("Question 4: the average number of days on the market.")

average_market_stay = session.query(
    func.datediff("Units", Transaction.transactionDate, Listing.date)
    ).select_from(Listing).join(Transaction).filter(Listing.sold == True).all()
print(pd.read_sql(average_market_stay, session.bind))

print("Question 5:  the average selling price")
sql5 = text("select SUM(price) / COUNT(sold) from listing where sold == True")
results = engine.execute(sql5)

for record in results:
    print("\n", record[0])

# TESTING: Only house with id 0, 1, 2, 4, 5, 6, 7, 11 are sold --> SUM(price) = 1,010,000 / 8 sold houses = 126250