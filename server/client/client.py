import socket
from threading import Thread

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

IP_ADDRESS = '127.0.0.1'
PORT = 8080
BUFFER_SIZE = 4096
SERVER = None

    
def musicWindow():
    global window
    
    window = Tk()
    window.title("Music Window")    
    window.geometry("300x300")
    window.configure(bg="lightSkyBlue")
    
    selectlabel = Label(window,text="Select Song" , bg='LightSkyBlue',font=("Helvetica",0))
    selectlabel.place(x=2,y=1)

    listBox = Listbox(window,height=10,width=39,activestyle='dotbox',bg='LightSkyblue',font=("Helvetica",0))
    listBox.place(x=10,y=10)

    Scrollbar1 = Scrollbar(listBox)
    Scrollbar1.place(relheight = 1,relx=1)
    Scrollbar1.config(command=listBox.yview)

    playButton = Button(window,text="Play",width=10,bd=1,bg="SkyBlue",font=("Helvetica",0))
    playButton.place(x=30,y=200)

    Stop = Button(window,text="Stop",bd=1,width=10,bg="SkyBlue",font=("Helvetica",0))        
    Stop.place(x=200,y=200)

    Upload = Button(window,text="Upload",bd=1,width=10,bg="SkyBlue",font=("Helvetica",0))        
    Upload.place(x=30,y=250)

    Download = Button(window,text="Download",bd=1,width=10,bg="SkyBlue",font=("Helvetica",0))        
    Download.place(x=4,y=200)  



def setup():

    global PORT
    global IP_ADDRESS
    global SERVER


    SERVER  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
    
setup()

