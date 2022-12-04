# cs162-database-management-system

This database system helps the real estate company maintain their own company
- There are different offices all over the country
- One seller can sell multiple houses, and one buyer can buy multiple houses
- Agents correspond to one or more offices
- When a transaction is made, the agent responsible for the house will get commission based on a sliding commission rate

## Execution

Please follow these commands to execute the code
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 models.py
python3 insert.py
python3 queries.py
```

## Data Normalization

This schema design satisfies all requirements of at least Third Normal Form

- 1NF:
    - Each column shows unique attributes with unique names
    - No dependencies in the order of columns in the table

- 2NF:
    - All columns depend on only the primary key
    - No composite keys

- 3NF:
    - No transitive dependency: one table only refers to id in another table for the sake of relationships. For example, table Listing will not contain information about Agent or Seller, yet refers to them through id

## Indices

I index almost all unique columns only in main table (Office, Buyer, Seller, Agent) except for the primary key column to optimize searching and queries

## Transactions

I define a function to capture what happens in a transaction (compute commission rate, add entry to Commission table and Transaction table)