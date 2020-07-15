import os
from tkinter.filedialog import askdirectory
 
import pygame
from mutagen.id3 import ID3
from tkinter import *
 
root = Tk()
root.minsize(300,300)
 
 
listofsongs = []
realnames = []
 
v = StringVar()
songlabel = Label(root,textvariable=v,width=35)
 
index = 0
 
def directorychooser():
 
    directory = askdirectory()
    os.chdir(directory)
 
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
 
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
 
 
            listofsongs.append(files)
 
 
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
 
directorychooser()
 
def updatelabel():
    global index
    global songname
    v.set(realnames[index])

 
def playsong(event):
    global index
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


'''def choosesong(event):
    global index
    w=event.widget
    curr_index=int (w.curselection()[0])
    value=w.get(curr_index)
    pygame.mixer.music.load(listofsongs[curr_index])
    pygame.mixer.music.play()'''   
 
def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
 
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    

def decrease_volume(event):
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.1) 


def increase_volume(event):
    pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.1)
 
 
label = Label(root,text='Music Player')
label.pack()
 
listbox = Listbox(root)
listbox.pack()
 
realnames.reverse()
 
for items in realnames:
    listbox.insert(0,items)
 
realnames.reverse()

playbutton= Button(root,text = 'Play')
playbutton.pack() 
 
nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()
 
previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()
 
stopbutton = Button(root,text='Stop Music')
stopbutton.pack()


pygame.mixer.music.set_volume(0.1)
volumebutton1= Button(root,text='Decrease Volume')
volumebutton1.pack()

volumebutton2= Button(root,text='Increase Volume')
volumebutton2.pack()
 
 
playbutton.bind("<Button-1>",playsong)
#listbox.bind("<Button-1>", choosesong)
nextbutton.bind("<Button-1>",nextsong)                                     
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
volumebutton1.bind('<Button-1>',decrease_volume)
volumebutton2.bind('<Button-1>',increase_volume)
 
songlabel.pack()
 
root.mainloop()
