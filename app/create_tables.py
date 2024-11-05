import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    database="factory_and_sale"
)

cursor = db.cursor()

# Check if the table exists and create it if it doesn't
create_table_query = """
CREATE TABLE IF NOT EXISTS MediaContent (
    media_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    media_type VARCHAR(50),
    media_path VARCHAR(255),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
"""

cursor.execute(create_table_query)
db.commit()

print("Table 'MediaContent' has been checked/created.")

# Close the connection
cursor.close()
db.close()
