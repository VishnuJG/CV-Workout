import PySimpleGUI as sg
from reps import repsfun
from legcurls import legscurlfun
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

def statsfun(vname):
    layout1 = [
        [sg.Button('Armreps', button_color="Brown", font=("Arial", 13)),
        sg.Button('Legcurls', button_color="Brown", font=("Arial", 13))],
        [sg.Canvas(key='figCanvas'), sg.Canvas(key='figCanvas2')],
        [sg.Button('Exit')]
    ]
    # layout=[[sg.Column(layout1, scrollable=True,  vertical_scroll_only=True)]]
    window1 = sg.Window('Statistics', layout1, margins=(0, 0),
                        resizable=True, element_justification="c").Finalize()
    window1.Maximize()

    canvas = None
    canvas2 = None
    while True:
        event1, values1 = window1.read()
        if event1 in (sg.WIN_CLOSED, 'Exit') or event1 == 'Exit':
            break
        elif event1 == 'Armreps':
            datevar, ly, ry, lmax, lmin, rmax, rmin = dbgetinfo(vname, "armreps")
            fig = plt.figure()
            # plt.bar(x, y, color='Orange', width=0.1)
            plt.plot(datevar, ly, color='red', marker='o', label="left")
            plt.plot(datevar, ry, color='blue', marker='o', label="right")
            plt.grid(True)
            plt.title("Armreps stats")
            plt.xlabel('date')
            plt.ylabel('reps')
            plt.legend()
            # plt.ylim([0, 100])
            if(canvas):
                delete_figure_agg(canvas)
            canvas = draw_figure(window1['figCanvas'].TKCanvas, fig)
            
            fig2 = plt.figure()
            # plt.bar(x, y, color='Orange', width=0.1)
            plt.plot(datevar, lmax, color='red', marker='o', label="left_max")
            plt.plot(datevar, lmin, color='blue', marker='o', label="left_min")
            plt.plot(datevar, rmax, color='green', marker='o', label="right_max")
            plt.plot(datevar, rmin, color='orange', marker='o', label="right_min")
            plt.grid(True)
            plt.title("Armreps stats")
            plt.xlabel('date')
            plt.ylabel('reps')
            plt.legend()
            # plt.ylim([0, 100])
            if(canvas2):
                delete_figure_agg(canvas2)
            canvas2 = draw_figure(window1['figCanvas2'].TKCanvas, fig2)
        elif event1 == 'Legcurls':
            datevar, ly, ry, lmax, lmin, rmax, rmin = dbgetinfo(vname, "legcurls")
            fig = plt.figure()
            # plt.bar(x, y, color='Orange', width=0.1)
            plt.plot(datevar, ly, color='red', marker='o', label="left")
            plt.plot(datevar, ry, color='blue', marker='o', label="right")
            plt.grid(True)
            plt.title("Legcurls stats")
            plt.xlabel('date')
            plt.ylabel('curls')
            plt.legend()
            # plt.ylim([0, 100])
            if(canvas):
                delete_figure_agg(canvas)
            canvas = draw_figure(window1['figCanvas'].TKCanvas, fig)

            fig2 = plt.figure()
            # plt.bar(x, y, color='Orange', width=0.1)
            plt.plot(datevar, lmax, color='red', marker='o', label="left_max")
            plt.plot(datevar, lmin, color='blue', marker='o', label="left_min")
            plt.plot(datevar, rmax, color='green', marker='o', label="right_max")
            plt.plot(datevar, rmin, color='orange', marker='o', label="right_min")
            plt.grid(True)
            plt.title("Legcurls stats")
            plt.xlabel('date')
            plt.ylabel('reps')
            plt.legend()
            # plt.ylim([0, 100])
            if(canvas2):
                delete_figure_agg(canvas2)
            canvas2 = draw_figure(window1['figCanvas2'].TKCanvas, fig2)

    window1.close()
