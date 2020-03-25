#########################################################################
#########################################################################
#########################################################################

##Conrad Pereira

##Statistics Modules

##Performs one sample mean T Test
##Given:
##      Mean
##      Null Hypothesis
##      Standard Deviation
##  --> Computes T-Stat
##      Confidence Level
##      Compares T-critcal value with T-stat
##  --> Provides correct solution
##Performs other Tests...

#########################################################################
#########################################################################
#########################################################################
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from subprocess import call

class callModules(object):
    
    def __init__(self, path ='/Users/conradpereira/Desktop/Statistics-Modules/TTestModule.py'):
        self.path = path
        
    def callTTestModule(self):
        call(["Python3", "{}".format(self.path)])




    
def clickedTtest():
    callMod = callModules()
    callMod.callTTestModule()
def clicked():
    messagebox.showinfo('Click one ofSeveral software modules that automatically performs different statistical tests. (One Sample T Test, Two independent samples t-test, One-way ANOVA, Regression Coefficient Testing, etc.')
window = tk.Tk()
window.title("Statistics Modules") 
window.geometry('1000x1000')

btn = Button(window,text='Help', command=clicked)
btn.grid(column=0,row=30)

lblTitle = Label(window, text= "Statistical Modules")
lblTitle.grid(column=1, row = 0)

btnTtest = Button(window, text="Single Sample T Test", command=clickedTtest)
btnTtest.grid(column=1, row=4)

btnTtest = Button(window, text="Two Sample T Test", command=clickedTtest)
btnTtest.grid(column=1, row=6)

btnTtest = Button(window, text="Regression Coefficeint T Test", command=clickedTtest)
btnTtest.grid(column=1, row=8)

btnTtest = Button(window, text="ANOVA", command=clickedTtest)
btnTtest.grid(column=1, row=10)

window.mainloop()
