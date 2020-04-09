from os import startfile
import subprocess
import time
import datetime
import csv
from pynput.keyboard import Key,Controller
from pynput.mouse import Button
from pynput.mouse import Controller as mController

def get_period():
    periods = {
        1 : (datetime.time(7,30),datetime.time(8,40)),
        2 : (datetime.time(8,40),datetime.time(9,25)),
        3 : (datetime.time(9,25),datetime.time(10,15)),
        4 : (datetime.time(10,15),datetime.time(11,15)),
        5 : (datetime.time(11,15),datetime.time(12,15)),
    }
    for period in periods:
        if periods[period][0] <= datetime.datetime.now().time() < periods[period][1]:
            return  period
    print("No class at the moment")
    input("press Enter to exit...")

def get_id():
    day = int(datetime.datetime.now().strftime("%w"))+1
    print("Day:",datetime.datetime.now().strftime("%A"))
    period = get_period()
    print(f"Period : {period}")
    with open("timetable.csv","r") as timetable:
        timetableReader = list(csv.reader(timetable))
        id = timetableReader[day][period]
        print(f"id : {id}")
        # if id == "8240514257":
        #     return "9014681675" if (input("Sir/Maam: ")).lower() == "maam" else "8240514257"
        return id

def get_pass(id):
    with open("passwords.csv","r") as passwords:
        reader = csv.DictReader(passwords)
        for row in reader:
            if row["id"] == id:
                print("subject:", row["sub"])
                subprocess.run("clip",universal_newlines = True, input = row["password"])
                return row["password"]

def zoom(id,password):
    keyboard = Controller()
    mouse = mController()
    if get_period() == 1:
        startfile(r"C:\Users\Lenovo\AppData\Roaming\Zoom\bin\Zoom.exe")
        time.sleep(2)
    else:
        with keyboard.pressed(Key.alt_l):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
    time.sleep(0.5)
    mouse.position = 690,380
    mouse.click(Button.left)
    time.sleep(2.5)
    mouse.position = 690,343
    mouse.click(Button.left)
    keyboard.type(id)
    keyboard.press(Key.enter)
    time.sleep(4)
    keyboard.type(password)
    keyboard.press(Key.enter)           

zoomId = get_id()
zoomPass = get_pass(zoomId)
zoom(zoomId,zoomPass)
