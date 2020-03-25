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
import tkinter.font as tkFont
from subprocess import call


class callModules(object):

    def __init__(self, path ='/Users/conradpereira/Desktop/UCSC/Projects/Statistics-Modules/TTestModule.py'):
        self.path = path

    def callTTestModule(self):
        #path ='/Users/conradpereira/Desktop/UCSC/Projects/Statistics-Modules/TTestModule.py'
        call(["Python3", "{}".format(self.path)])

class callModules2(object):
    def __init__(self, path = '/Users/conradpereira/Desktop/UCSC/Projects/Statistics-Modules/2SampleTTestModule.py'):
        self.path = path
    def callTTestModule2(self):
        call(["Python3", "{}".format(self.path)])

class callModules3(object):
    def __init__(self, path = '/Users/conradpereira/Desktop/UCSC/Projects/Statistics-Modules/RegCoeffModule.py'):
        self.path = path
    def callRegcoeff(self):
        call(["Python3", "{}".format(self.path)])

class callModules4(object):
    def __init__(self, path = '/Users/conradpereira/Desktop/UCSC/Projects/Statistics-Modules/ANOVAModule.py'):
        self.path = path
    def callAnova(self):
        call(["Python3", "{}".format(self.path)])

class callModules5(object):
    def __init__(self, path = '/Users/conradpereira/Desktop/UCSC/Projects/Statistics-Modules/MeasuresModule.py'):
        self.path = path
    def callMeasures(self):
        call(["Python3", "{}".format(self.path)])


def clickedTtest():
    callMod = callModules()
    callMod.callTTestModule()

def clickedTtest2():
    callMod = callModules2()
    callMod.callTTestModule2()

def clickedRegcoeff():
    callMod = callModules3()
    callMod.callRegcoeff()

def clickedAnova():
    callMod = callModules4()
    callMod.callAnova()

def clickedMeasures():
    callMod = callModules5()
    callMod.callMeasures()


def clicked(): #HELP
    messagebox.showinfo('Help','Click one ofSeveral software modules that automatically performs different statistical tests. (One Sample T Test, Two independent samples t-test, One-way ANOVA, Regression Coefficient Testing, etc.')



window = tk.Tk()

window.title("Statistics Modules")
window.geometry('1000x1000')
stats = tk.PhotoImage(file="Stats.png")
w1 = tk.Label(window, image=stats)
w1.grid(column=4, row =0)



btn = Button(window,text='Help', command=clicked)
btn.grid(column=0,row=30)

lblTitle = Label(window, text= "Statistical Modules")
lblTitle.grid(column=1, row = 0)

btnMeasures= Button(window, text="Measures of Central Tendancy", command=clickedMeasures)
btnMeasures.grid(column=1, row=2)

btnTtest = Button(window, text="Single Sample T Test", command=clickedTtest)
btnTtest.grid(column=1, row=4)

btnTtest2 = Button(window, text="Two Sample T Test", command=clickedTtest2)
btnTtest2.grid(column=1, row=6)

btnRegcoeff = Button(window, text="Regression Coefficient T Test", command=clickedRegcoeff)
btnRegcoeff.grid(column=1, row=8)

btnAnova = Button(window, text="ANOVA", command=clickedAnova)
btnAnova.grid(column=1, row=10)

window.mainloop()
