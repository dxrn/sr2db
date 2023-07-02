# sr2db
Generates an sqlite database from Amazon Seller Central Business Reports.

## Setup
1. Download Amazon Seller Central Business Reports by month (ex. 1/1/2022-1/31/2022). Preferably, download the files and place them into to the csv folder. 

Note: The report will need to include and exclude certain categories for it to work properly. See File Format below.

2. Copy and paste the path of each month into the ```paths.json``` file. (ex. "January":" /january-seller-report.csv")

## Generating a database
```python sr2db.py --d azr 2022```

This will create a database named azr with 2022 as the year.

## Generating a csv
```python sr2db.py --c azr.db```

This will create a formatted csv of all historical demand per month by child ASIN.

## File Format
Unfortunately, AZ reports will need to be exported with the following categories in this order, this can be changed via the Show/Hide Columns sidebar:

Parent Asin  
Child Asin  
Title  
SKU  
Sessions - Total  
Sessions Percentage - Total  
Page Views - Total  
Page Views Percentage - Total  
Featured Offer (Buy  Box) Percentage  
Units Ordered  
Units Ordered - B2B  
Ordered Product Sales  
Ordered Product Sales - B2B  
Total Order Items  
Total Order Items - B2B  

[Image](https://i.imgur.com/lNPMdnt.png)