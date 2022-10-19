# sr2db
Generates an sqlite database from Amazon Seller Central Business Reports.

## Setup
1. Download Amazon Seller Central Business Reports by month (ex. 1/1/2022-1/31/2022). Preferably, download the files and place them into to the csv folder. 

2. Copy and paste the path of each month into the ```paths.json``` file. (ex. "January":" /january-seller-report.csv")

## Generating a database
```python sr2db.py --c azr 2022```

This will create a database named azr with 2022 as the year.

## Generating a csv
```python sr2db.py --d azr.db```

This will create a formatted csv of all historical demand per month by child ASIN.