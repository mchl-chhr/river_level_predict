import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data/EcrRiv.sqlite')
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all rows
rows = cursor.fetchall()

# Print rows
for row in rows:
    print(row)

# Close the connection
conn.close()
