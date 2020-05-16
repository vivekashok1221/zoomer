# zoomer

### requirements:
- pynput
>download pynput by entering ```pip install pynput``` in cmd

- docx
>download docx by entering ```pip install python-docx``` in cmd

#### make sure ```timetable.csv``` and ```passwords.csv``` are in the same folder as zoomer.py
note: "timetable.csv" and "passwords.csv" have not been uploaded due to security reasons. 

## Command line interface
A CLI has been added for additional functionality.
The following list will help illustrate their use.

Name         | Command             | Description
-------------|---------------------|----------------------------------
 help        | -h, --help          |show help message and exit
manual       |-m *subject*           |manually enter the subject      
ultramanual  |-M *id password*      |manually enter id and password
 append      |-a *subject id password*|append data to passwords.csv
changepass   |-p *subject new_password*,<br> --passwd *subject new_password*|change the password corresponding to the subject                   
updatepass   |-u *path*, <br>--updatepass *path*|updates passwords.csv with data extracted from docx at path
getmousepos  |-gmp, --getmousepos|command to get mouse position and update data.ini

