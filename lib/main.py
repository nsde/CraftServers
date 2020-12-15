import os
import sys
import new
import install
import tkinter
win = tkinter.Tk()
win.title("CraftServers")

def newInstallation():
    install.create()

def newProject():
    new.newProject()

tkinter.Label(win, text="CraftServers").pack()
tkinter.Button(win, text="Install a new software", command=newInstallation).pack()
tkinter.Button(win, text="Create a new project", command=newProject).pack()
tkinter.Button(win, text="Exit", command=sys.exit, fg="red").pack()

win.mainloop()