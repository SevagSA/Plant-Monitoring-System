import sqlite3

######PSEUDOCODE START########
$current_rfid_tag = getCurrentRFIDTag() #<---Retrieve RFID tag obtained from user.
######PSEUDOCODE END##########

#Connect to database
conn = sqlite3.connect('userSettings.db')
print("Connection to database 'userSettings.db' established successfully! (Source: '1.get_name.py')\n")

#Create a cursor
c = conn.cursor() #'c' is cursor

c.execute("SELECT name FROM users WHERE user_id LIKE {$current_rfid_tag}")

user_name = c.fetchone()

print(user_name)

#Commit the command
conn.commit()

#Close the connection
conn.close()