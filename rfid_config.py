import sqlite3

con = sqlite3.connect('userSettings.db')

cur = con.cursor()


def get_temp_threshold(rfid_tag):
    cur.execute(
        f'SELECT temperature_threshold FROM preference_dict WHERE tag="{rfid_tag}"')
    return cur.fetchone()[0]


def get_photoresistor_threshold(rfid_tag):
    cur.execute(
        f'SELECT photoresistor_threshold FROM preference_dict WHERE tag="{rfid_tag}"')
    return cur.fetchone()[0]


def set_temp_threshold(rfid_tag, threshold):
    cur.execute(
        f'UPDATE preference_dict SET temperature_threshold = {threshold} WHERE tag="{rfid_tag}"')
    con.commit()


def set_photoresistor_threshold(rfid_tag, threshold):
    cur.execute(
        f'UPDATE preference_dict SET photoresistor_threshold = {threshold} WHERE tag="{rfid_tag}"')
    con.commit()


def get_auth_user():
    cur.execute('SELECT user_tag FROM authenticated_user')
    return cur.fetchone()[0]


def set_auth_user(rfid_tag):
    cur.execute(
        f'UPDATE authenticated_user SET user_tag = {rfid_tag}')
    con.commit()


con.close()
