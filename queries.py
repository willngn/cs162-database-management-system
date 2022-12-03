from models import *
from sqlalchemy.orm import sessionmaker 
Session = sessionmaker(bind=engine)
session = Session()

# Question 1: top 5 offices with the most sales for that month.

