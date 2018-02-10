import sqlite3

#dbname = str(input("Enter Database Name: "))
#dbname+=".db"
db = sqlite3.connect('dbname.db')


#print("Connecting to Database: {}".format(dbname))
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                       phone TEXT, email TEXT unique, password TEXT)
''')

name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'

# A very secure password
password1 = '12345'

name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

# Insert user 1
cursor.execute('''INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
print('First user inserted')

# Insert user 2
cursor.execute('''INSERT INTO users(name, phone, email, password)
                  VALUES(?,?,?,?)''', (name2,phone2, email2, password2))
print('Second user inserted')

db.commit()
