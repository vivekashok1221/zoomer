import time
import datetime
import csv
from pynput.keyboard import Key,Controller,Events

def get_id():
    day = int(datetime.datetime.now().strftime("%w"))+1
    period=int(input("Enter the period:"))
    with open("timetable.csv","r") as timetable:
        timetableReader = list(csv.reader(timetable))
        id = timetableReader[day][period]
        # if id == "8240514257":
        #     return "9014681675" if (input("Sir/Maam: ")).lower() == "maam" else "8240514257"
        print(id)
        return id

def get_pass(id):
    with open("passwords.csv","r") as passwords:
        reader = csv.DictReader(passwords)
        for row in reader:
            if row["id"] == id:
                return row["password"]

def zoom(id,password):
    keyboard = Controller()
    with Events() as events:
            for event in events:
                if event.key == Key.home:
                    keyboard.type(id)
                    keyboard.press(Key.enter)
                    break
    time.sleep(5)
    keyboard.type(password)
    keyboard.press(Key.enter)           

zoomId = get_id()
zoomPass = get_pass(zoomId)
zoom(zoomId,zoomPass)
