from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

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

print("Question 3: the commission that each estate agent must receive")
# we already have a separate Commission table
sql3 = text("SELECT name, email, SUM(commission) FROM (SELECT * FROM Agent Join Commission ON Agent.id == Commission.agentID) GROUP BY agentID ORDER BY SUM(Commission) DESC")
results = engine.execute(sql3)

for record in results:
    print("\n", record)

print("Question 4: the average number of days on the market.")
