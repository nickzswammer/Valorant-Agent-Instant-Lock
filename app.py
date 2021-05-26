# Import module
from tkinter import ttk
from tkinter import *
from ttkthemes import ThemedTk
import pyautogui, time
import sys
import webbrowser
from PIL import ImageTk, Image

#Create Location Variables
lock_in = (953, 808)

agents = {
    'astra': (661,922),
    'breach': (758,933),
    'brimstone': (829,923),
    'cypher': (916,926),
    'jett': (1004,927),
    'killjoy': (1084,932),
    'omen': (1166,923),
    'phoenix': (1248,922),
    'raze': (667,1003),
    'reyna': (736,1004),
    'sage': (841,1018),
    'skye': (927,1009),
    'sova': (1008,1004),
    'viper':(1085,998),
    'yoru': (1176,1010),

}

# Create object
root = ThemedTk()
root.title('Valorant Instant Agent Lock Tool')


#Set Title and Photo
root.set_theme('equilux')
photo = PhotoImage(file='Jett_icon.png')
root.iconphoto(False, photo)

root.after(1, lambda: root.focus_force())


# Adjust size
root.geometry( "500x450" )
root.resizable(width=False, height=False)

#Image
valorant = ImageTk.PhotoImage(Image.open('val_icon.png'))
valorant_label = Label(root, image=valorant)
valorant_label.pack()

label223 = Label( root , text = "" )
label223.pack()


#Functions


#Function to Show Text
def show():
    label.config( text = f'Selected Agent: {clicked.get()}' )
    current=clicked.get()

#Function to Click Mouse On Key Press
def click(self):
    pyautogui.moveTo(500,500)
    pyautogui.click()

    pyautogui.moveTo(100,100)
    pyautogui.click()
    root.withdraw()
    root.deiconify()


def stop(self):
    pyautogui

#Function to close application
def close(self):
    root.withdraw()
    sys.exit()

#Hyperlink Function
def callback(url):
   webbrowser.open_new_tab(url)

#Get Agent
def get_agent(self):
    agent = agents[f'{(clicked.get()).lower()}']
    pyautogui.moveTo(agent[0],agent[1])
    pyautogui.click()

    pyautogui.moveTo(lock_in[0],lock_in[1])
    pyautogui.click()
    root.withdraw()
    root.deiconify()


# Dropdown Agent menu options
options = [
    'Astra',
    "Astra",
    "Breach",
    "Brimstone",
    "Cypher",
    "Jett",
    "Killjoy",
    "Omen",
    'Phoenix',
    'Raze',
    'Reyna',
    'Sage', 
    'Skye',
    'Sova',
    'Viper',
    'Yoru'
]
  
# datatype of menu text
clicked = StringVar()
  
# Create Dropdown menu
drop = ttk.OptionMenu( root , clicked , *options )
drop.pack()

#Making Space
label = Label( root , text = "" )
label.pack()

# Create button, it will change label text
button = ttk.Button( root , text = "Choose Agent" , command = show)
button.pack()

# Create Labels
label22 = Label( root , text = "" )
label22.pack()

instructions_label = Label(root, text='Instructions:\n Choose an Agent above then Hold F5 to start insta-locking. Press F10 to stop. \n\n(Make sure you are about to load into the agent select screen).')
instructions_label.pack()

label2332 = Label( root , text = " \n" )
label2332.pack()

plug_label = Label(root, text='Created by swammer. Visit my Github')
plug_label.pack()

link = Label(root, text='Here', fg='blue')
link.pack()
link.bind('<Button-1>' , lambda e: callback('https://github.com/nickzswammer'))
link


#Key Bindings #CHANGE THESE TO PYAUTOGUI REDDIT
root.bind('<F10>', close)
root.bind('<F5>', get_agent)
root.bind('<F4>', stop)

# Execute tkinter
root.mainloop()