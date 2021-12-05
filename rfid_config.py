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


print(get_temp_threshold("131504313"))
print(get_temp_threshold("124103131100"))
print(get_photoresistor_threshold("131504313"))
print(get_photoresistor_threshold("124103131100"))


def set_temp_threshold(rfid_tag, threshold):
    cur.execute(
        f'UPDATE preference_dict SET temperature_threshold = {threshold} WHERE tag="{rfid_tag}"')
    con.commit()


def set_photoresistor_threshold(rfid_tag, threshold):
    cur.execute(
        f'UPDATE preference_dict SET photoresistor_threshold = {threshold} WHERE tag="{rfid_tag}"')
    con.commit()


# TODO you can delete this. This is just a working example
# set_temp_threshold("131504313", 22)
# set_temp_threshold("124103131100", 25)
# set_photoresistor_threshold("131504313", 600)
# set_photoresistor_threshold("124103131100", 540)


print(get_temp_threshold("131504313"))
print(get_temp_threshold("124103131100"))
print(get_photoresistor_threshold("131504313"))
print(get_photoresistor_threshold("124103131100"))


con.close()
