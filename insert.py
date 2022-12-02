from models import *
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.sql import select

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

office_agent_keys = ['officeID', 'agentID']
office_agent_info = []

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
    [12, "Anu", "anu@gmail.com"],
]

house_keys = ['id', 'officeID', 'sellerID', 'bedrooms', 'bathrooms', 'price', 'zipcode', 'sold']
house_info = [
    [0, 3, 6, 2, 2, 120000.50, 94102, False],
    [1, 2, 6, 2, 2, 120000.50, 94102, False],
    [2, 4, 6, 2, 2, 120000.50, 94102, False],
    [3, 5, 6, 2, 2, 120000.50, 94102, False],
    [4, 1, 6, 2, 2, 120000.50, 94102, False],
    [5, 0, 6, 2, 2, 120000.50, 94102, False],
    [6, 8, 6, 2, 2, 120000.50, 94102, False],
    [7, 9, 6, 2, 2, 120000.50, 94102, False],
    [8, 2, 6, 2, 2, 120000.50, 94102, False],
    [9, 6, 6, 2, 2, 120000.50, 94102, False],
    [10, 4, 6, 2, 2, 120000.50, 94102, False],
    [11, 1, 6, 2, 2, 120000.50, 94102, False],
    [12, 0, 6, 2, 2, 120000.50, 94102, False],
], 