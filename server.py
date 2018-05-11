import os
import socket
from tkinter import *

master = Tk()

def callback():
    os.popen("python -m http.server 80")
    print(socket.gethostbyname(socket.gethostname()))

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()