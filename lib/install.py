"""This program is for installing the .jar files for servers.
"""

import os
import tkinter
import requests

from functools import partial

serverInfo = {
    "Vanilla_1-16-4":       "https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar",
    "Paper_1-12-2":         "https://papermc.io/ci/job/Paper/lastSuccessfulBuild/artifact/paperclip.jar",
    "Paper_1-15-2_391":     "https://papermc.io/api/v1/paper/1.15.2/391/download",
    "Paper_1-16-4_325":     "https://papermc.io/api/v1/paper/1.16.4/325/download",
}


def create():
    win = tkinter.Tk()
    win.title("Set up server")

    def setup(serverID):
        win.title("Downloading server files...")

        url = serverInfo[serverID]
        serverData = requests.get(url).content
        
        with open(os.getcwd() + "\\servers" + serverID + "\\server.jar", 'wb') as f:
            f.write(serverData)

        win.title("Downloading server files...")
        win.title("Server menu")
    
    for key in serverInfo:
        try:
            os.mkdir(os.getcwd() + "\\servers\\" + key)

        except Exception as errorCode:
            if "already exists" not in str(errorCode):
                print("Couldn't create folder " + key + " because " + str(errorCode))

        tkinter.Button(win, text=key, command=partial(setup, key)).pack()
    
    def close():
        win.destroy()

    tkinter.Button(win, text="Cancel", fg="red", command=close).pack()

    win.mainloop()