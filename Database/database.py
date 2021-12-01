# class Database:
#     def __init__(self):
#         conn = sqlite3.connect('userSettings.db')
#         print("Connection to database 'userSettings.db' established successfully! (Source: '__init__(self)')\n")

#         #Create a cursor
#         c = conn.cursor() #'c' is cursor

#         many_users = [
#         ('124103131100', 'Ali', 18, 200),
#         ('53125461236', 'Sebastian', 20, 400),
#         ('31126391236', 'Nicolas', 15, 100),
#         ('131504313', 'Sevag', 24, 500)
#         ]
#         c.executemany("INSERT INTO users VALUES (?,?,?,?)", many_users[0]) #Comment line
#         c.execute("INSERT INTO users VALUES ('98765432182', 'Samad', 22, 800)") #Comment line

#         c.execute("SELECT * FROM users")


#         print("Tables created successfully!")

#         #Commit the command
#         conn.commit()

#         #Close the connection
#         conn.close()

#     def getAllUsers():
#         import sqlite3

#         #Connect to database
#         conn = sqlite3.connect('userSettings.db')
#         print("Connection to database 'userSettings.db' established successfully! (Source: 'getAllUsers()')\n")

#         #Create a cursor
#         c = conn.cursor() #'c' is cursor

#         #many_users = [
#         #('12341251512', 'Ali', 18, 200),
#         #('53125461236', 'Sebastian', 20, 400),
#         #('31126391236', 'Nicolas', 15, 100),
#         #('17342542182', 'Sevag', 24, 500)
#         #]
#         #c.executemany("INSERT INTO users VALUES (?,?,?,?)", many_users[0]) #Comment line
#         #c.execute("INSERT INTO users VALUES ('98765432182', 'Samad', 22, 800)") #Comment line

#         c.execute("SELECT * FROM users")

#         #print(c.fetchone())
#         #print(c.fetchAll())
#         #print(c.fetchmany(3))

#         users = c.fetchall()
#         print("ALL USERS IN DATABASE:")
#         print(users)
#         print("All users fetched successfully!\n")

#         print("ALL NAMES OF USERS IN DATABASE:")
#         for row in users:
#             print(row[1])
#         print("All users iteratively fetched successfully!\n")

#         print("Command(s) executed successfully!")

#         #Commit the command
#         conn.commit()

#         #Close the connection
#         conn.close()


#     def get_name(rfid_tag):
#         import sqlite3

#         #Connect to database
#         conn = sqlite3.connect('userSettings.db')
#         print("Connection to database 'userSettings.db' established successfully! (Source: 'get_name(rfid_tag)')\n")

#         #Create a cursor
#         c = conn.cursor() #'c' is cursor

#         c.execute(f"SELECT name FROM users WHERE user_id LIKE {rfid_tag}")

#         user_name = c.fetchone()

#         #Commit the command
#         conn.commit()

#         #Close the connection
#         conn.close()

#         return user_name

#     def get_favorite_temperature(rfid_tag):
#         import sqlite3

#         #Connect to database
#         conn = sqlite3.connect('userSettings.db')
#         print("Connection to database 'userSettings.db' established successfully! (Source: 'get_favorite_temperature(rfid_tag)')\n")

#         #Create a cursor
#         c = conn.cursor() #'c' is cursor

#         c.execute("SELECT favorite_temperature FROM users WHERE user_id LIKE {rfid_tag}")

#         favorite_temperature = c.fetchone()

#         #Commit the command
#         conn.commit()

#         #Close the connection
#         conn.close()

#         return favorite_temperature

#     def set_favorite_temperature(rfid_tag, updated_temp):
#         import sqlite3

#         #Connect to database
#         conn = sqlite3.connect('userSettings.db')
#         print("Connection to database 'userSettings.db' established successfully! (Source: 'set_favorite_temperature(rfid_tag, update_temp)')\n")

#         #Create a cursor
#         c = conn.cursor() #'c' is cursor

#         c.execute(f"UPDATE users SET favorite_temperature = {updated_temp} WHERE user_id LIKE {rfid_tag}")

#         #Commit the command
#         conn.commit()

#         #Close the connection
#         conn.close()

#     def get_favorite_light_intensity(rfid_tag):
#         import sqlite3

#         #Connect to database
#         conn = sqlite3.connect('userSettings.db')
#         print("Connection to database 'userSettings.db' established successfully! (Source: 'get_favorite_light_intensity(rfid_tag)')\n")

#         #Create a cursor
#         c = conn.cursor() #'c' is cursor

#         c.execute("SELECT favorite_light_intensity FROM users WHERE user_id LIKE {rfid_tag}")

#         favorite_light_intensity = c.fetchone()

#         #Commit the command
#         conn.commit()

#         #Close the connection
#         conn.close()

#         return favorite_light_intensity

#     def set_favorite_light_intensity(rfid_tag, updated_light_intensity):
#         import sqlite3

#         #Connect to database
#         conn = sqlite3.connect('userSettings.db')
#         print("Connection to database 'userSettings.db' established successfully! (Source: 'set_favorite_light_intensity(rfid_tag, updated_light_intensity)')\n")

#         #Create a cursor
#         c = conn.cursor() #'c' is cursor

#         c.execute(f"UPDATE users SET favorite_light_intensity = {updated_light_intensity} WHERE user_id LIKE {rfid_tag}")

#         #Commit the command
#         conn.commit()

#         #Close the connection
#         conn.close()
