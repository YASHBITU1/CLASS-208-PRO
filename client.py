#-----------Bolierplate Code Start -----
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None


def openChatWindow():

   
    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()

    window.title('Messenger')
    window.geometry("500x350")

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Enter Your Name", font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    name = Entry(window,width =30,font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window,text="Connect to Chat Server",bd=1, font = ("Calibri",10))
    connectserver.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Active Users", font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    connectButton=Button(window,text="Connect",bd=1, font = ("Calibri",10))
    connectButton.place(x=282,y=160)

    disconnectButton=Button(window,text="Disconnect",bd=1, font = ("Calibri",10))
    disconnectButton.place(x=350,y=160)

    refresh=Button(window,text="Refresh",bd=1, font = ("Calibri",10))
    refresh.place(x=435,y=160)
    
    chatWindow = Label(window,text="Chat",font = ("Calibri",10))
    chatWindow.place(x=10,y=180)

    textArea = Text(window,height=6,width=67,font = ("Calibri",10))
    textArea.place(x=10,y=200)
    
    scrollbar2 = Scrollbar(textArea)
    scrollbar2.place(relheight=1,relx=1)
    scrollbar2.config(command=textArea.yview)
    
    input = Entry(window,width=25,font = ("Calibri",15))
    input.pack()
    input.place(x=120,y=305)
    
    
    sendButton = Button(window,text="SEND",bd=1,font = ("Calibri",10))
    sendButton.place(x=400,y=305)
    
    attachButton = Button(window,text="ATTACH & SEND",bd=1,font = ("Calibri",10))
    attachButton.place(x=10,y=305)
    
    pathDisplay = Label(window,text="",fg="red",bd=1,font = ("Calibri",10))
    pathDisplay.place(x=10,y=315)
    
    
    
  
  
  
  
  
    window.mainloop()




def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    openChatWindow()

setup()
