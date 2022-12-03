from models import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import pandas as pd
from sqlalchemy import text

Session = sessionmaker(bind=engine)
session = Session()

# Question 1: top 5 offices with the most sales for that month.
# referece: https://www.geeksforgeeks.org/how-to-execute-raw-sql-in-sqlalchemy/

sql1 = text("SELECT Office.name, Count(Listing.officeID) FROM Office Join Listing ON Office.id == Listing.officeID GROUP BY Listing.officeID ORDER BY Count(Listing.officeID) DESC LIMIT 5")
results = engine.execute(sql1)

for record in results:
    print("\n", record)

