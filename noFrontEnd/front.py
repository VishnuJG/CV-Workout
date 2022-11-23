
import PySimpleGUI as sg
from reps import repsfun
from legcurls import legscurlfun
from stats import statsfun
from dbFuns import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')

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
        [sg.Button('Set', button_color = "Brown", font=("Arial", 13)),sg.Button('Start', button_color = "Green", font=("Arial", 13)),sg.Button('Stats', button_color = "Blue", font=("Arial", 13)),sg.Button('Exit', button_color = "Red", font=("Arial", 13))],
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
                if(res[0]>0 or res[1]>0):
                    dbUpdatefun(vname, "armreps_left", res[1])
                    dbUpdatefun(vname, "armreps_right", res[0])
                dbUpdatefunsetting(vname, "armleft_minangle", res[2])
                dbUpdatefunsetting(vname, "armright_minangle", res[3])
                dbUpdatefunsetting(vname, "armleft_maxangle", res[4])
                dbUpdatefunsetting(vname, "armright_maxangle", res[5])
                window['-RES-'].update("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")
                sg.Popup("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")

            elif values['-OMENU-']=="Leg Curls":
                
                res=legscurlfun(values['LeftSlider'], values['RightSlider'], values['LowLeftSlider'], values['LowRightSlider'])
                if(res[0]>0 or res[1]>0):
                    dbUpdatefun(vname, "legcurls_left", res[1])
                    dbUpdatefun(vname, "legcurls_right", res[0])
                window['-RES-'].update("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")
                sg.Popup("Result : LEFT->"+str(res[1])+"\tRIGHT->"+str(res[0]), text_color="Green")

            else:
                window['-RES-'].update("Please select an exercise to perform", text_color="Red")
                # sg.Popup('Please select an exercise to perform', text_color="Red")
        elif event=='Stats':
            # layout1=[
            #     [sg.Button('Armreps', button_color = "Brown", font=("Arial", 13)),sg.Button('Legcurls', button_color = "Brown", font=("Arial", 13))],
            #     [sg.Canvas(key='figCanvas')],
            #     [sg.Button('Exit')] 
            # ]

            # window1=sg.Window('Statistics', layout1, finalize=True, resizable=True, element_justification="right")

            # canvas=None
            # while True:
            #     event1,values1=window1.read()
            #     if event1 in (sg.WIN_CLOSED, 'Exit') or event1=='Exit':
            #         break
            #     elif event1=='Armreps':
            #         x,y = dbgetinfo(vname, "armreps")
            #         fig = plt.figure()
            #         plt.plot(x,y,color='Orange', marker='o')
            #         plt.grid(True)
            #         plt.title("Armreps stats")
            #         plt.xlabel('date')
            #         plt.ylabel('reps')
            #         if(canvas):
            #             delete_figure_agg(canvas)
            #         canvas=draw_figure(window1['figCanvas'].TKCanvas, fig)
            #     elif event1=='Legcurls':
            #         x,y = dbgetinfo(vname, "legcurls")
            #         fig = plt.figure()
            #         plt.plot(x,y,color='Orange', marker='o')
            #         plt.grid(True)
            #         plt.title("Legcurls stats")
            #         plt.xlabel('date')
            #         plt.ylabel('curls')
            #         if(canvas):
            #             delete_figure_agg(canvas)
            #         canvas=draw_figure(window1['figCanvas'].TKCanvas, fig)
            # window1.close()
            statsfun(vname)

    window.close()