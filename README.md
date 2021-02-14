# zoomer
This is a program that will enter the meeting id and password for zoom meetings, and I use it for my online classes. 

This implementation uses mysql rather than CSV due to project requirements of my Computer Science Project 2020-21.

### requirements:
- pynput
- docx (*optional, comment the import*)

**note: running `pip install -r requirements.txt` will install both pacakges.**

### setting it up:
Type ```python zoomer.py -gmp``` to set the position of join button.
Make a ```timetable.csv``` and ```passwords.csv``` according to your needs (An example has been provided).
A timetable is not necessary as a simple command line interface has been provided which will let you use the program more flexibily.

#### make sure ```timetable.csv``` and ```passwords.csv``` are in the same folder as zoomer.py
~~note: "timetable.csv" and "passwords.csv" have not been uploaded due to security reasons~~
note: "password.csv" has been filled with my meeting id and meeting password and I consent to its use for demonstrative purposes.

## Command line interface
A CLI has been added for additional functionality.
The following list will help illustrate their use.

Name         | Command             | Description
-------------|---------------------|----------------------------------
 help        | -h, --help          |show help message and exit
 reset       | --reset              | resets zoomer.py and clears the database.
 getmousepos  |-gmp, --getmousepos|command to get mouse position and update data.ini
manual       |-m *subject*           |manually enter the subject
 append      |-a *subject id password*|append data to passwords.csv
changepass   |-p *subject new_password*,<br> --passwd *subject new_password*|change the password corresponding to the subject                   
updatepass   |-u *path*, <br>--updatepass *path*|updates passwords.csv with data extracted from docx at path


