from pynput.mouse import Controller
from pynput.keyboard import Key,Events
def setup():
    print("\n*************************************************************\n")
    print("It seems that you are running zoomer.py for the first time since the path to Zoom.exe has not been found")
    print("This program will guide you to setup zoomer.py\n\nstep 1:")
    print("Install pynput library by typing 'pip install pynput' in the cmd")
    input("Press enter when done...")

    print("\n\nstep 2:")
    path = input("Enter the path of the zoom executable (don't forget to add \"Zoom.exe\" at the end):")
    
    print('''\nstep 3:\nNow we are going to initialise mouse coordinates.
Open zoom and hover the mouse cursor above the \"join\" button and press <CTRL>.''')

    mouse = Controller()
    def get_coord():
        with Events() as events:
            for event in events:                
                if event.key == Key.ctrl_l:
                    posn = mouse.position
                    return str(posn)[1:-1]

    with open('passwords.csv','a') as pw, open('timetable.csv','a') as t:           
        pw.write('\n'+path)
        t.write('\n'+ get_coord())

    print("Restart zoomer")
    input("Press enter to exit...")
    raise SystemExit
