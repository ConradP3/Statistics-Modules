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

def clicked():
    messagebox.showinfo('Two Sample TTest Module Description', 'Software module to  automatically perform two sample mean T Test given the sample means, null hypothesis, standard deviations, and confidence interval. Assumptions: Sample sizes are sufficiently large enough to perform Test')

def confidenceLevel(TCritCon):
    if(TCritCon == 90):
        TCritCon = 1.65
    elif(TCritCon ==95):
        TCritCon = 1.95
    elif(TCritCon == 99):
        TCritCon = 2.58

def clickedTest():
    Samplemean = float(txtSamplemean.get())
    Samplemean2 = float(txtSamplemean2.get())
    Nullhyp = float(txtNull.get())
    Variance = float(txtVar.get())
    Variance2 = float(txtVar2.get())
    Samplesize=float(txtSamplesize.get())
    Samplesize2=float(txtSamplesize2.get())

    TCrit=float(txtConfidencelvl.get())
    #TCrit = float(comboConfidencelvl.get())

    TStat = (Samplemean-Samplemean2-Nullhyp)/(math.sqrt((Variance/Samplesize)+(Variance2/Samplesize2)))

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

window.title("Two Sample T-Test")
window.geometry('1000x1000')

w1 = tk.Label(window, image=logo)
w1.grid(column=1, row =0)

lblSamplemean = Label(window, text ="Sample Mean")
lblSamplemean.grid(column=0, row=6)

txtSamplemean = Entry(window,width=20)
txtSamplemean.grid(column=1, row = 6)

lblSamplemean2 = Label(window, text ="2nd Sample Mean")
lblSamplemean2.grid(column=0, row=7)

txtSamplemean2 = Entry(window,width=20)
txtSamplemean2.grid(column=1, row = 7)

lblNullhyp = Label(window, text ="Null Hypothesis")
lblNullhyp.grid(column=0, row=8)

txtNull = Entry(window,width=20)
txtNull.grid(column=1, row = 8)


lblVariance = Label(window, text ="Variance")
lblVariance.grid(column=0, row=10)

txtVar = Entry(window,width=20)
txtVar.grid(column=1, row = 10)

lblVariance2 = Label(window, text ="2nd Sample's Variance")
lblVariance2.grid(column=0, row=11)

txtVar2 = Entry(window,width=20)
txtVar2.grid(column=1, row = 11)

txtSamplesize = Entry(window,width=20)
txtSamplesize.grid(column=1, row = 12)

lblSamplesize = Label(window, text ="Sample Size")
lblSamplesize.grid(column=0, row=12)

txtSamplesize2 = Entry(window,width=20)
txtSamplesize2.grid(column=1, row = 14)

lblSamplesize2 = Label(window, text ="2nd Sample Size")
lblSamplesize2.grid(column=0, row=14)

##comboConfidencelvl = Combobox(window)
##comboConfidencelvl['values']= (1.65,1.95,2.58)
##comboConfidencelvl.grid(column=1, row = 12)
txtConfidencelvl = Entry(window,width=20)
txtConfidencelvl.grid(column=1, row = 16)

lblConfidencelvl = Label(window, text ="Confidence Level (Enter 90, 95 or 99)")
lblConfidencelvl.grid(column=0, row=16)

##explanation = """Software module to perform a T Test"""
##lbl = Label(window, text=explanation, )
##lbl.grid(column=0, row=1)

lblans = Label(window, text = "")
lblans.grid(column=1, row=20)


btnTtest = Button(window, text="Two Sample T Test", command=clickedTest)

btnTtest.grid(column=1, row=18)

btn = Button(window,text='TTest Module Explanation', command=clicked)

btn.grid(column=0,row=0)

window.mainloop()
