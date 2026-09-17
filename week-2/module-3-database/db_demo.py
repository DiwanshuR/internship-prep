import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
)
''')

# delete to execute the code again
cursor.execute('DELETE FROM users')

# Insert data into the table
cursor.execute('''
INSERT INTO users (name, email) VALUES (?, ?)
''', ('John Cena', 'john.cena@example.com'))

data_to_insert = [
    ('Alice Smith', 'alice.smith@example.com'),
    ('Bob Johnson', 'bob.johnson@example.com')
]
cursor.executemany('''
INSERT INTO users (name, email) VALUES (?, ?)
''', data_to_insert)

# Commit the changes
connection.commit()

# Query the data
cursor.execute('SELECT * FROM users')

# Fetch all results - extracts the rows into a list of tuples
users = cursor.fetchall()

cursor.execute(''' SELECT name, email FROM users WHERE id = ? ''', (1,))
user1 = cursor.fetchall()


for user in users:
    print(f'ID: {user[0]}, Name: {user[1]}, Email: {user[2]}')
    
for user in user1:
    print(f'Name: {user[0]}, Email: {user[1]}')

# close the connection
cursor.close()
connection.close()
