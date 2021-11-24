import sqlite3

#Connect to database
conn = sqlite3.connect('userSettings.db')
print("Connection to database 'userSettings.db' established successfully!\n")

#Create a cursor
c = conn.cursor() #'c' is cursor

many_users = [
	('12341251512', 'Ali', 18, 200),
	('53125461236', 'Sebastian', 20, 400),
	('31126391236', 'Nicolas', 15, 100),
	('17342542182', 'Sevag', 24, 500)
]
#c.executemany("INSERT INTO users VALUES (?,?,?,?)", many_users[0]) #Comment line
#c.execute("INSERT INTO users VALUES ('98765432182', 'Samad', 22, 800)") #Comment line

c.execute("SELECT * FROM users")

#print(c.fetchone())
#print(c.fetchAll())
#print(c.fetchmany(3))

users = c.fetchall()
print("ALL USERS IN DATABASE:")
print(users)
print("All users fetched successfully!\n")

print("ALL NAMES OF USERS IN DATABASE:")
for row in users:
	print(row[1])
print("All users iteratively fetched successfully!\n")

print("Command(s) executed successfully!")

#Commit the command
conn.commit()

#Close the connection
conn.close()