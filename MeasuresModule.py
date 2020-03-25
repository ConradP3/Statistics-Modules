#########################################################################
#########################################################################
#########################################################################

##Conrad Pereira

##2 Sample T Test Module

##Performs 2 sample mean T Test
##Given:
##      Mean
##      2nd Mean
##      Null Hypothesis
##      Standard Deviations
##      Sample Sizes
##  --> Computes T-Stat
##      Confidence Level
##      Compares T-critcal value with T-stat
##  --> Provides correct solution

#########################################################################
#########################################################################
#########################################################################

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import numpy as np
from scipy import stats
import math

def clicked(): #HELP
    messagebox.showinfo('Measures of Central Tendancy','Enter values necessary to compute mean, median, mode, etc.')

def clickedMeasure():
    sampleSize= float(txtSamplesize.get())
    sum = float(txtSum.get())

    computeMean(sum, sampleSize)

    # + '  median: ' + str(median) +' mode: '+ str(mode))
def computeMean(sum, n):
    #for x in range(n):
    #    sumTotal=sumtotal+obs[x]
    mean = sum/n

    lblMean.configure(text = 'mean: ' + str(mean))


window = tk.Tk()

window.title("Measures of Central Tendancy")
window.geometry('1000x1000')

btn = Button(window,text='Explanation', command=clicked)
btn.grid(column=0,row=0)

lblTitle = Label(window, text= "Measures of Central Tendancy")
lblTitle.grid(column=1, row = 0)

btnMeasures= Button(window, text="Calculate Measures of Central Tendancy", command=clickedMeasure)
btnMeasures.grid(column=1, row=1)

txtSum = Entry(window,width=20)
txtSum.grid(column=1, row = 2)

lblSum = Label(window, text ="Sum of Observations")
lblSum.grid(column=0, row=2)

txtSamplesize = Entry(window,width=20)
txtSamplesize.grid(column=1, row = 3)

lblSamplesize = Label(window, text ="Sample Size")
lblSamplesize.grid(column=0, row=3)

lblMean = Label(window, text= '')
lblMean.grid(column=1,row=20)


window.mainloop()
