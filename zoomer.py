from os import startfile
import subprocess
import time
import datetime
import csv
from pynput.keyboard import Key,Controller
from pynput.mouse import Button
from pynput.mouse import Controller as mController
import setupHelper

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
    raise SystemExit

def get_id(file):
    file.seek(0)
    period = get_period()
    timetableReader = list(csv.reader(file))
    day = int(datetime.datetime.now().strftime("%w"))+1
    id = timetableReader[day][period]
    print("Day:",datetime.datetime.now().strftime("%A"))
    print(f"Period : {period}")
    print(f"id : {id}")
    return id

def get_pass(id,file):
    file.seek(0)
    reader = csv.DictReader(passwords)
    for row in reader:
        if row["id"] == id:
            print("subject:", row["sub"])
            subprocess.run("clip",universal_newlines = True, input = row["password"])
            return row["password"]

def zoom(id,password,path,joinposn):
    keyboard = Controller()
    mouse = mController()
    if get_period() == 1:
        startfile(path)
        time.sleep(1) #
    else:
        with keyboard.pressed(Key.alt_l):
            keyboard.press(Key.tab)
            keyboard.release(Key.tab)
    time.sleep(0.5) #
    mouse.position = joinposn
    mouse.click(Button.left)
    time.sleep(1) #
    keyboard.type(id)
    keyboard.press(Key.enter)
    time.sleep(3.5) #
    keyboard.type(password)
    keyboard.press(Key.enter)           

with open('timetable.csv','r') as timetable, open('passwords.csv','r') as passwords:
    path = passwords.readlines()[-1] #r'C:\Users\Lenovo\AppData\Roaming\Zoom\bin\Zoom.exe'
    if path[-3:] == 'cs2':
        setupHelper.setup()
    else:
        joinposn = timetable.readlines()[-1].split(', ') #list(coordinates of join button)
        zoomId = get_id(timetable)
        zoomPass = get_pass(zoomId,passwords)
        
zoom(zoomId,zoomPass,path,joinposn)
