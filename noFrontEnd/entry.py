import re
import PySimpleGUI as sg
from reps import repsfun
from legcurls import legscurlfun
from front import frontdef
from dbFuns import *
from newUser import *

dbHealthCheck()

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

sg.theme('SandyBeach')

layout = [
    [sg.Text('Please enter your Name and Email')],
    [sg.Text("Name", size=(15, 1)), sg.InputText(key="-NAME-")],
    # [sg.Text('Age', size =(15, 1)), sg.InputText(key="-AGE-")],
    [sg.Text('Email', size=(15, 1)), sg.InputText(key="-EMAIL-")],
    # [sg.Text("Disclaimer!", size =(15, 1), text_color="Red", font=("Times New Roman", 20))],
    [sg.Button('Login', button_color='Green'), sg.Button(
        'EXIT', button_color="Red"), sg.Button('New User', button_color="Blue")],
    [sg.Text(size=(50, 2), key='-RES-', font=("Arial", 10))]
]


window = sg.Window('Login window', layout, resizable=True,
                   element_justification='c').Finalize()
window.Maximize()
# event, values = window.read()
# window.close()
# if event=='Login':
#     if dbVerificationfun(values['-NAME-'])==values['-EMAIL-']:
#         frontdef(values['-NAME-'])
#     else:
#         window['-RES-'].update("Wrong email ID and name, please check again", text_color="Red")
# else:
#     pass

flag = 0
tempval = ""
while True:
    event, values = window.read()
    if event == 'Login':

        if values['-NAME-'] == "" or values['-EMAIL-'] == "":
            window['-RES-'].update("Invalid input for Username/Email",
                                   text_color="Red")
        elif not re.fullmatch(regex, values['-EMAIL-']):
            window['-RES-'].update("Invalid Email", text_color="Red")
        else:
            if dbVerificationfun(values['-NAME-']) == values['-EMAIL-']:
                # frontdef(values['-NAME-'])
                tempval = values['-NAME-']
                flag = 1
                break
            else:
                window['-RES-'].update(
                    "Wrong email ID or User name, please check again", text_color="Red")
                flag = 0
    elif event == 'New User':
        newUserFun()
    else:
        break

window.close()
if flag:
    disclaimer_agreement = 0
    disclaimer_text_column1 = [[sg.Text("App Disclaimer", size=(20, 1), text_color="Red", font=("Times New Roman", 20))],
                               [sg.Text("The information provided by PES University on this application is for general informational purposes only. All information on this application is provided in good faith, however we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability, or completeness of any information on this application. UNDER NO CIRCUMSTANCE SHALL WE HAVE ANY LIABILITY TO YOU FOR ANY LOSS OR DAMAGE OF ANY KIND INCURRED AS A RESULT OF THE USE OF THIS APPLICATION OR RELIANCE ON ANY INFORMATION PROVIDED ON THIS APPLICATION. YOUR USE OF THIS APPLICATION AND YOUR RELIANCE ON ANY INFORMATION ON THIS APPLICATION IS SOLELY AT YOUR OWN RISK.", size=(50, 10))],
                               [sg.Text("Professional Disclaimer", size=(20, 1), text_color="Green", font=("Times New Roman", 20))],
                               [sg.Text("This Application does not contain any fitness advice. The fitness information provided here is for the general information for educational purposes only and is not a substitute for professional advice. We do not provide any kind of fitness advice and you have to consult professional experts before taking any actions based upon the information provided. THE USE OR RELIANCE OF ANY INFORMATION CONTAINED ON THIS APPLICATION IS SOLELY AT YOUR OWN RISK. AND WE WILL NOT BE RESPONSIBLE FOR ANY LOSS.", size=(50, 10))]
                               ]

    layout1 = [[sg.Text("Disclaimer!", size=(15, 1), text_color="Red", font=("Times New Roman", 20))],
               [sg.Column(disclaimer_text_column1, scrollable=True, vertical_scroll_only=True)],
               
               [sg.Button('Agree', button_color='Green'), sg.Button('Reject', button_color="Red")]]
    window_disclaimer = sg.Window(
        'Agreement window', layout1, resizable=True, element_justification='c')
    
    while True:
        event, values = window_disclaimer.read()
        if event == 'Agree':
            disclaimer_agreement = 1

            break
        else:
            break
    if disclaimer_agreement:
        window_disclaimer.close()
        frontdef(tempval)
