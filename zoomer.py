import time
import datetime
import csv
from pynput.keyboard import Key,Controller,Events

def get_period():
    periods = {
        6 : (datetime.time(22,30),datetime.time(23,0)),
        1 : (datetime.time(7,30),datetime.time(8,40)),
        2 : (datetime.time(8,40),datetime.time(9,25)),
        3 : (datetime.time(9,25),datetime.time(10,15)),
        4 : (datetime.time(10,15),datetime.time(11,15)),
        5 : (datetime.time(11,15),datetime.time(12,15)),
    }
    for period in periods:
        if periods[period][0] <= datetime.datetime.now().time() < periods[period][1]:
            return  period

def get_id():
    day = int(datetime.datetime.now().strftime("%w"))+1
    period = get_period() 
    with open("timetable.csv","r") as timetable:
        timetableReader = list(csv.reader(timetable))
        id = timetableReader[day][period]
        # if id == "8240514257":
        #     return "9014681675" if (input("Sir/Maam: ")).lower() == "maam" else "8240514257"
        return id

def get_pass(id):
    with open("passwords.csv","r") as passwords:
        reader = csv.DictReader(passwords)
        for row in reader:
            if row["id"] == id:
                return row["password"]

def zoom(id,password):
    keyboard = Controller()
    keyboard.type(id)
    keyboard.press(Key.enter)
    time.sleep(5)
    keyboard.type(password)
    keyboard.press(Key.enter)           

zoomId = get_id()
zoomPass = get_pass(zoomId)
zoom(zoomId,zoomPass)
