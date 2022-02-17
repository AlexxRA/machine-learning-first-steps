import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *

global points
points = []

class Point:
    x1 = 0
    x2 = 0
    y = 0

# WINDOW INIT
gui = Tk()
gui.title("Perceptron test")
gui.geometry("800x750")

#FIG INIT
fig = Figure(figsize=(5,4), dpi = 100)
plt = fig.add_subplot(111)
plt.set_xlim([-5,5])
plt.set_ylim([-5,5])
plt.plot([0,0], [-5,5],color="gray")
plt.plot([-5,5],[0,0],color="gray")

#CHART INIT
chart = FigureCanvasTkAgg(fig, gui)
chart.draw()
chart.get_tk_widget().grid(column = 0, row = 5)

# W1 INPUT
Label(gui, text="Valor W1").grid(row=0, column=0)
w1_entry = Entry(gui, width=8)
w1_entry.grid(row=0, column=1)

#W2 INPUT
Label(gui, text="Valor W2").grid(row=1, column=0)
w2_entry = Entry(gui, width=8)
w2_entry.grid(row=1, column=1)

#W3 INPUT
Label(gui, text="Valor theta").grid(row=2, column=0)
theta_entry = Entry(gui, width=8)
theta_entry.grid(row=2, column=1)

#Calculate line
def calculate_line():
    # fig.clear(True)
    w1=float(w1_entry.get())
    w2=float(w2_entry.get())
    theta=float(theta_entry.get())

    #draw line
    y = []
    Fx = np.arange(-5,5)
    for p in Fx:
        y_prima = (((-w1)/(w2))*p)+(theta/w2)
        y.append(y_prima)
    # plt.cla()
    plt.plot(Fx, y)
    
    #funcion de activacion
    for p in points:
        v = (w1+p.x1) + (w2*p.x2) - theta
        if v > 0:
            plt.plot(p.x1, p.x2, marker="o", color="green")
        else:
            plt.plot(p.x1, p.x2, marker="o", color="red")
    
    chart.draw()


# Update Button
calculate_btn = Button(gui, text="Calculate", command = calculate_line)
calculate_btn.grid(row=3, column=1)
gui.bind("<Return>", calculate_line)


#GET POINTS ON CHART
def click_get_coords(event):
    if event.button == 3:
        point = Point()
        plt.plot(event.xdata, event.ydata, 'ob')
        point.x1 = event.xdata
        point.x2 = event.ydata
        points.append(point)
        for j in points:
            print(str(j.x1) + " - " + str(j.x2))

    chart.draw()

fig.canvas.mpl_connect('button_press_event', click_get_coords)



gui.mainloop()