import sqlite3
import constants

con = sqlite3.connect('userSettings.db',check_same_thread=False)

cur = con.cursor()


def get_temp_threshold(rfid_tag):
    if rfid_tag == "None" or not rfid_tag in constants.valid_rfid_tags:
        return 0
    cur.execute(f'SELECT temperature_threshold FROM preference_dict WHERE tag="{rfid_tag}"')
    return cur.fetchone()[0]


def get_photoresistor_threshold(rfid_tag):
    if rfid_tag == "None" or not rfid_tag in constants.valid_rfid_tags:
            return 0
    cur.execute(
        f'SELECT photoresistor_threshold FROM preference_dict WHERE tag="{rfid_tag}"')
    return cur.fetchone()[0]


def set_temp_threshold(rfid_tag, threshold):
    cur.execute(
        f'UPDATE preference_dict SET temperature_threshold = {threshold} WHERE tag="{rfid_tag}"')
    con.commit()


def set_photoresistor_threshold(rfid_tag, threshold):
    print("in set", threshold)
    cur.execute(
        f'UPDATE preference_dict SET photoresistor_threshold = {threshold} WHERE tag="{rfid_tag}"')
    con.commit()


def get_auth_user():
      with open("current_rfid_tag.txt", "r+") as file:
        return file.read()


def set_auth_user(rfid_tag):
    with open("current_rfid_tag.txt", "w") as file:
        file.write(rfid_tag)
        file.close() 

def get_user_name(tag):
    cur.execute(f'SELECT name FROM preference_dict WHERE tag="{tag}"')
    return cur.fetchone()[0]
