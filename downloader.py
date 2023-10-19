from pytube import YouTube
from tkinter import *

import sys

#root window
root = Tk()
root.title("Youtube downloader")
root.geometry("500x200")

#variables for strong values
outputVar = StringVar()
radioVar= StringVar()
linkVar = StringVar()

def download():
    global outputVar
    global radioVar
    global linkVar

    print("in download")
    outputVar.set("downloading " + stream.title)
    link = linkVar.get()
    type = radioVar.get()

    SAVE_PATH = "~/Downloads"
    try:
        yt = YouTube(link)

        stream = object()
        print(type)
    except:
        outputVar.set("bad link, try again")

    if type == "video":
        print("video selected")
        stream = yt.streams.get_highest_resolution()
    else: 
        print("audio selected")
        stream = yt.streams.get_audio_only()
    
    try: 
        stream.download(output_path= SAVE_PATH)
        outputVar.set("download completed")
    except:
        outputVar.set("error, try again")
        print("error")



#main frame
frm = Frame(root)
frm.pack()

#radio buttons
radioVar= StringVar()
radioVar.set("video")

radioframe = Frame(frm)
videoRadio = Radiobutton(radioframe, text="Video", variable=radioVar, value="video", ).grid(column=0, row=0)
audioRadio = Radiobutton(radioframe, text="Audio", variable=radioVar, value="audio").grid(column=1, row=0)

#link lable and entry
headerText = Label(frm, text="youtube downloader").pack()

linkFrame = Frame(frm, pady= 10)
linkFrame.pack()
linklabel = Label(linkFrame, text="Link:").grid(column=0, row=0)
linkEntry  = Entry(linkFrame, textvariable= linkVar).grid(column=1, row=0)
buttonSubmit = Button(
    linkFrame, 
    text="download", 
    command= download,
    bg="blue").grid(column=2, row=0)

#radio buttons

radioVar.set("video")

radioframe = Frame(frm)
videoRadio = Radiobutton(radioframe, text="Video", variable=radioVar, value="video", ).grid(column=0, row=0)
audioRadio = Radiobutton(radioframe, text="Audio", variable=radioVar, value="audio").grid(column=1, row=0)
radioframe.pack()

#progresss output
progressOutput = Label(frm, textvariable=outputVar)
progressOutput.pack()

root.mainloop()