"""This program is for creating a new server.
"""

import os
import tkinter
import install
def newProject():
    win = tkinter.Tk()
    win.title("New project")

    def projectCreate():
        projectName = projectNameInp.get()
        print(projectName)
        os.mkdir(os.getcwd() + "\\projects\\" + projectName)

        with open (os.getcwd() + "\\projects\\" + projectName + "\\info", "w") as f:
            f.write()


    projectNameTxt = tkinter.Label(win, text="Project name")
    projectNameTxt.pack()

    projectNameInp = tkinter.Entry(win)
    projectNameInp.pack()

    projectNameTxt = tkinter.Label(win, text="Project name")
    projectNameTxt.pack()

        # datatype of menu text 
    clicked = tkinter.StringVar() 
    
    # initial menu text 
    clicked.set( "Monday" ) 
    
    # Create Dropdown menu 
    drop = tkinter.OptionMenu(win, clicked , *) 
    drop.pack() 

    projectCreateBtn = tkinter.Button(win, text="Create", command=projectCreate)
    projectCreateBtn.pack()

    win.mainloop()