import re
import PySimpleGUI as sg
from reps import repsfun
from legcurls import legscurlfun
from front import frontdef
from dbFuns import dbHealthCheck, dbVerificationfun, dbNewUserfun

# Initialize database

dbHealthCheck()

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

sg.theme('SandyBeach')

layout = [
    [sg.Text('Please enter your Name and Email')],
    [sg.Text("Name", size=(15, 1)), sg.InputText(key="-NAME-")],
    [sg.Text('Email', size=(15, 1)), sg.InputText(key="-EMAIL-")],
    [sg.Button('Login', button_color='Green'), sg.Button('EXIT', button_color="Red"), sg.Button('New User', button_color="Blue")],
    [sg.Text(size=(50, 2), key='-RES-', font=("Arial", 10))]
]

window = sg.Window('Login window', layout, resizable=True, element_justification='c').Finalize()
window.Maximize()

while True:
    event, values = window.read()
    if event == 'Login':
        if values['-NAME-'] == "" or values['-EMAIL-'] == "":
            window['-RES-'].update("Invalid input for Username/Email", text_color="Red")
        elif not re.fullmatch(regex, values['-EMAIL-']):
            window['-RES-'].update("Invalid Email", text_color="Red")
        else:
            if dbVerificationfun(values['-NAME-']) == values['-EMAIL-']:
                frontdef(values['-NAME-'])
                break
            else:
                window['-RES-'].update("Wrong email ID or User name, please check again", text_color="Red")
    elif event == 'New User':
        newUserFun()
    else:
        break

window.close()
