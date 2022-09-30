import re
import PySimpleGUI as sg
from reps import repsfun
from legcurls import legscurlfun
from front import frontdef
from dbFuns import *
from newUser import *

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

sg.theme('SandyBeach') 

layout = [
    [sg.Text('Please enter your Name and Email')],
    [sg.Text("Name", size =(15, 1)), sg.InputText(key="-NAME-")],
    # [sg.Text('Age', size =(15, 1)), sg.InputText(key="-AGE-")],
    [sg.Text('Email', size =(15, 1)), sg.InputText(key="-EMAIL-")],
    [sg.Text("Disclaimer!", size =(15, 1), text_color="Red", font=("Times New Roman", 20))],
    [sg.Button('Accept', button_color='Green'), sg.Button('EXIT',button_color="Red" ), sg.Button('New User', button_color="Blue")],
    [sg.Text(size=(50,2), key='-RES-', font=("Arial", 10))]
]


window = sg.Window('Login window', layout)
# event, values = window.read()
# window.close()
# if event=='Accept':
#     if dbVerificationfun(values['-NAME-'])==values['-EMAIL-']:
#         frontdef(values['-NAME-'])
#     else:
#         window['-RES-'].update("Wrong email ID and name, please check again", text_color="Red")
# else:
#     pass

flag = 0
tempval=""
while True:
    event,values=window.read()
    if event=='Accept':
        
        if values['-NAME-'] == "" or values['-EMAIL-'] == "":
            window['-RES-'].update("Invalid input for Username/Email", text_color="Red")
        elif not re.fullmatch(regex, values['-EMAIL-']):
            window['-RES-'].update("Invalid Email", text_color="Red")
        else:
            if dbVerificationfun(values['-NAME-'])==values['-EMAIL-']:
                # frontdef(values['-NAME-'])
                tempval=values['-NAME-']
                flag=1
                break;
            else:
                window['-RES-'].update("Wrong email ID or User name, please check again", text_color="Red")
                flag=0
    elif event == 'New User':
        newUserFun()
    else:
        break;
        
window.close()
if flag:
    frontdef(tempval)