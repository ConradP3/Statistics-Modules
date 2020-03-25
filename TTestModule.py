#########################################################################
#########################################################################
#########################################################################

##Conrad Pereira

##T Test Module

##Performs one sample mean T Test
##Given:
##      Mean
##      Null Hypothesis
##      Standard Deviation
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


def clicked():
    messagebox.showinfo('One Sample TTest Module Description', 'Software module to  automatically perform one sample mean T Test given the sample mean, null hypothesis, standard deviation, and confidence interval. Assumptions: Sample size is sufficiently large enough to perform Test')

def confidenceLevel(TCritCon):
    if(TCritCon == 90):
        TCritCon = 1.65
    elif(TCritCon ==95):
        TCritCon = 1.95
    elif(TCritCon == 99):
        TCritCon = 2.58

def clickedTest():
    Samplemean = float(txtSamplemean.get())
    Nullhyp = float(txtNull.get())
    StandardDev = float(txtSd.get())
    Samplesize=float(txtSamplesize.get())
    TCrit=float(txtConfidencelvl.get())
    #TCrit = float(comboConfidencelvl.get())
    
    TStat = (Samplemean-Nullhyp)/(StandardDev/(math.sqrt(Samplesize)))

    if(TCrit == 90):
        TCrit = 1.65
    elif(TCrit ==95):
        TCrit = 1.95
    elif(TCrit == 99):
        TCrit = 2.58
    
    compareTvalues(TStat, TCrit)
    
    #ans = TStat
    #lblans.configure(text= ans)

def compareTvalues(TStat, TCrit):
    if(abs(TStat) > abs(TCrit)):
        lblans.configure(text= "We reject the null hypothesis " + "TStat = " + str(TStat) + " TCrit = " +str(TCrit))
    else: 
         lblans.configure(text= "We fail to reject the null hypothesis "+ "TStat = " + str(TStat) + " TCrit = " +str(TCrit))

window = tk.Tk()

logo = tk.PhotoImage(file="Ttest.png")

window.title("T-Test") 
window.geometry('1000x1000')

w1 = tk.Label(window, image=logo)
w1.grid(column=1, row =0)

lblSamplemean = Label(window, text ="Sample Mean")
lblSamplemean.grid(column=0, row=6)

txtSamplemean = Entry(window,width=20)
txtSamplemean.grid(column=1, row = 6)

lblNullhyp = Label(window, text ="Null Hypothesis")
lblNullhyp.grid(column=0, row=8)

txtNull = Entry(window,width=20)
txtNull.grid(column=1, row = 8)


lblStandarddev = Label(window, text ="Standard Deviation")
lblStandarddev.grid(column=0, row=10)

txtSd = Entry(window,width=20)
txtSd.grid(column=1, row = 10)

txtSamplesize = Entry(window,width=20)
txtSamplesize.grid(column=1, row = 12)

lblSamplesize = Label(window, text ="Sample Size")
lblSamplesize.grid(column=0, row=12)

##comboConfidencelvl = Combobox(window)
##comboConfidencelvl['values']= (1.65,1.95,2.58)
##comboConfidencelvl.grid(column=1, row = 12)
txtConfidencelvl = Entry(window,width=20)
txtConfidencelvl.grid(column=1, row = 14)

lblConfidencelvl = Label(window, text ="Confidence Level (Enter 90, 95 or 99)")
lblConfidencelvl.grid(column=0, row=14)

##explanation = """Software module to perform a T Test"""
##lbl = Label(window, text=explanation, )
##lbl.grid(column=0, row=1)

lblans = Label(window, text = "")
lblans.grid(column=1, row=20)


btnTtest = Button(window, text="Single Sample T Test", command=clickedTest)

btnTtest.grid(column=1, row=16)

btn = Button(window,text='TTest Module Explanation', command=clicked)

btn.grid(column=0,row=0)

window.mainloop()
