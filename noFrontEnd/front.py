
import PySimpleGUI as sg
from reps import repsfun
from legcurls import legscurlfun
from dbFuns import *


def frontdef(vname):
    sg.theme('SandyBeach')

    menudef=["Reps","Leg Curls"]

    layout = [
        
        [sg.Text("Welcome "+vname, size=(20,1), font=("Arial", 15))],
        [sg.Text("Choose an Exercise",size=(20,1), font=("Arial", 15)), sg.OptionMenu(values=["Reps","Leg Curls"], default_value="Select", key="-OMENU-")],
        
        [sg.Text('Left Curl stretch angle'), sg.Text(size=(15,1), key='-LEFT-', text_color="Red", font=("Arial", 15)),sg.Slider(orientation ='horizontal', default_value=160, key='LeftSlider', range=(0,180))],
        [sg.Text('Left Curl fold angle'), sg.Text(size=(15,1), key='-LOWLEFT-', text_color="Red", font=("Arial", 15)),sg.Slider(orientation ='horizontal', default_value=30, key='LowLeftSlider', range=(0,180))],

        [sg.Text('Right Curl stretch angle'), sg.Text(size=(15,1), key='-RIGHT-', text_color="Red", font=("Arial", 15)),sg.Slider(orientation ='horizontal', default_value=160, key='RightSlider',range=(0,180))],
        [sg.Text('Right Curl fold angle'), sg.Text(size=(15,1), key='-LOWRIGHT-', text_color="Red", font=("Arial", 15)),sg.Slider(orientation ='horizontal', default_value=30, key='LowRightSlider',range=(0,180))],
                    
            # [sg.Spin( values =[i for i in range(0, 181, 5)], key='spnMnt')],
        [sg.Button('Set', button_color = "Brown", font=("Arial", 13)),sg.Button('Start', button_color = "Green", font=("Arial", 13)),sg.Button('Exit', button_color = "Red", font=("Arial", 13))],
        [sg.Text(size=(50,2), key='-RES-', font=("Arial", 15))],
    ]

    window = sg.Window('Workout Setup Window', layout)
    while True:
        event,values=window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Set':
            window['-LEFT-'].update(values['LeftSlider'])
            window['-RIGHT-'].update(values['RightSlider'])
            window['-LOWLEFT-'].update(values['LowLeftSlider'])
            window['-LOWRIGHT-'].update(values['LowRightSlider'])


        elif event=='Start':
            window['-RES-'].update("Loading exercise...", text_color="Green")

            if values['-OMENU-']=='Reps':
                
                res=repsfun(values['LeftSlider'], values['RightSlider'], values['LowLeftSlider'], values['LowRightSlider'])
                dbUpdatefun(vname, "ARML", res[1])
                dbUpdatefun(vname, "ARMR", res[0])
                window['-RES-'].update("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")
                sg.Popup("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")

            elif values['-OMENU-']=="Leg Curls":
                
                res=legscurlfun(values['LeftSlider'], values['RightSlider'], values['LowLeftSlider'], values['LowRightSlider'])
                dbUpdatefun(vname, "LEGL", res[1])
                dbUpdatefun(vname, "LEGR", res[0])
                window['-RES-'].update("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")
                sg.Popup("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")

            else:
                window['-RES-'].update("Please select an exercise to perform", text_color="Red")
                # sg.Popup('Please select an exercise to perform', text_color="Red")
        
    window.close()