# Import module 
import sqlite3 

# Connecting to sqlite 
conn = sqlite3.connect('Sales.db') 

# Creating a cursor object using the  
# cursor() method 
cursor = conn.cursor() 

exec="""SELECT 
    o.order_id,
    o.order_date,
    c.first_name AS customer_first_name,
    c.last_name AS customer_last_name,
    s.first_name AS staff_first_name,
    s.last_name AS staff_last_name
FROM orders o
JOIN customers c WHERE o.customer_id = c.customer_id
JOIN staffs s WHERE o.staff_id = s.staff_id;
"""
try:
    cursor.execute(exec)
    print(cursor.fetchall())
except sqlite3.OperationalError as e:
    print(f"An error occurred:  {e}")

