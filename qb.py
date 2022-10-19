import os
import calendar
import csv
import sqlite3
import json

def create_db(array, DATABASE_NAME):
    if os.path.exists(f"database/{DATABASE_NAME}.db") == True:
        print("Found database file with same name")
        os.remove(f"database/{DATABASE_NAME}.db")
        print(f"Overwrote database: {DATABASE_NAME}.db")
    conn = sqlite3.connect(f"database/{DATABASE_NAME}.db")
    print(f"Created database: {DATABASE_NAME}.db")
    cursor = conn.cursor()
    
    cursor.execute("""CREATE TABLE main 
    (   
        date TEXT,
        parent_asin TEXT, 
        child_asin TEXT, 
        title TEXT,
        sku TEXT,
        sessions INTEGER,
        session_perc REAL,
        page_views INTEGER,
        page_views_perc REAL,
        buy_box_perc REAL,
        units_ordered INTEGER,
        units_ordered_b2b INTEGER,
        unit_session_perc REAL,
        unit_session_perc_b2b REAL,
        ordered_product_sales REAL,
        ordered_product_sales_b2b REAL,
        total_order_items INTEGER,
        total_order_items_b2b INTEGER
    )   
    """)

    cursor.executemany("""INSERT INTO main     
    (   
        date,
        parent_asin, 
        child_asin, 
        title,
        sku,
        sessions,
        session_perc,
        page_views,
        page_views_perc,
        buy_box_perc,
        units_ordered,
        units_ordered_b2b,
        unit_session_perc,
        unit_session_perc_b2b,
        ordered_product_sales,
        ordered_product_sales_b2b,
        total_order_items,
        total_order_items_b2b
    )   
     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);""", array)
    conn.commit()
    cursor.close()
    
def format_data(YEAR):
    paths_file = open("paths.json")
    paths = json.load(paths_file)
    files = []
    for k, v in paths.items():
        if v == '':
            print(f"Missing Month: {k}")
        else:
            files.append(v)

    data = []
    month = 1
    for i in files:
        with open(i,newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            row_count = 0
            for row in csvreader:
                for x in [5,7,8,11,12]:
                    row[x] = row[x].strip('%')
                for x in [13,14]:
                    row[x] = row[x].strip('$')
                    row[x] = row[x].replace(',','')

                row.insert(0, f"{YEAR}-{str(month).zfill(2)}-01")
                data.append(row)
                row_count += 1
        month += 1

    return data


def build_query(category,year):
    query = "SELECT parent_asin,child_asin, title, sku,"
    for x in range(1,13): 
        query += f'sum(CASE WHEN date = "{year}-{str(x).zfill(2)}-01" THEN {category} END) {calendar.month_abbr[x]}_{year}_{category},'
        if x == 12:
            query = query[:-1]
    
    query += " FROM main GROUP BY child_asin;"
    return query

def generate_csv(description, rows, DATABASE_NAME):
    if os.path.exists("result/")  == False:
        os.mkdir("result")

    with open(f"result/{DATABASE_NAME}_demand.csv", mode="w") as result:
        csvwriter = csv.writer(result, delimiter=",")
        header = []

        for i in range(len(description)):
            header.append(description[i][0])
        
        csvwriter.writerow(header)
        csvwriter.writerows(rows)
    print(f"CSV file: {DATABASE_NAME}_demand.csv generated.")

def monthly_demand(DATABASE_NAME):
    conn = sqlite3.connect(f"database/{DATABASE_NAME}")
    cursor = conn.cursor()
    cursor.execute("SELECT date from main ASC LIMIT 1;")
    rows = cursor.fetchall()
    year = rows[0][0][0:4]
    cursor.close()
    cursor = conn.cursor()
    query = build_query("units_ordered", year)
    cursor.execute(query)
    rows = cursor.fetchall()
    generate_csv(cursor.description, rows, DATABASE_NAME)

# TODO: Display stats
def stats(DATABASE_NAME):
    pass
