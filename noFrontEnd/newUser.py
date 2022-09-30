import PySimpleGUI as sg
import time
import re
from dbFuns import *

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def newUserFun():
    sg.theme('SandyBeach') 

    layout = [
        [sg.Text('Please enter your Name, Age, and Email')],
        [sg.Text("Name", size =(15, 1)), sg.InputText(key="-NAME-")],
        [sg.Text('Age', size =(15, 1)), sg.InputText(key="-AGE-")],
        [sg.Text('Email', size =(15, 1)), sg.InputText(key="-EMAIL-")],
        # [sg.Text("Disclaimer!", size =(15, 1), text_color="Red", font=("Times New Roman", 20))],
        [sg.Button('Create', button_color='Green'), sg.Button('Cancel',button_color="Red" )],
        [sg.Text(size=(50,2), key='-RES-', font=("Arial", 10))]
    ]

    window = sg.Window('New User Account Creating', layout)


    while True:
        event,values=window.read()
        if event=='Create':
            if dbVerificationfun(values['-NAME-']):
                window['-RES-'].update("User Name Already Exists", text_color="Red")

            elif dbVerificationfun(values['-EMAIL-']):
                window['-RES-'].update("Email Already Registered", text_color="Red")
            elif values['-NAME-'] == "" or values['-EMAIL-']=="":
                window['-RES-'].update("Invalid input for Username/Email", text_color="Red")
            elif not re.fullmatch(regex, values['-EMAIL-']):
                window['-RES-'].update("Invalid Email", text_color="Red")
            else:
                dbNewUserfun(values['-NAME-'], values['-AGE-'], values['-EMAIL-'])
                sg.Popup("Account Successfully Created", text_color="Green")
                window['-RES-'].update("Account Successfully created...", text_color="Green")
                # time.sleep(1)
                break;
        else:
            break;
            
    window.close()
    return