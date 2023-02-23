from tkinter import *
from pytube import YouTube
from pathlib import Path


#function 

def click(): #click button
    selection = file_type.get()
    convert(selection == 1)
    # time.sleep(2)
    # status_label.config(text="Waiting...")

    
def convert(isMP3):
    url = link.get()
    yt = YouTube(url) 
    status_label.config(text="Downloading",fg = "#00FF00")  
    try:
        downloader = yt.streams.filter(only_audio=True).get_audio_only() if isMP3 else yt.streams.get_highest_resolution()
        if isMP3:
            file = Path(downloader.download())
            state = file.rename(file.with_suffix('.mp3'))
        else:
            state = downloader.download()
    except:
        status_label.config(text="Wrong Link!",fg = "#FF0000")
    window.after(3000, lambda: status_label.config(text="Waiting...", fg= "#000000")) 
    window.after(3000, lambda:link.delete(0,END))


# Gui
window = Tk()
photo = PhotoImage(file = "metalogo.png")
window.iconphoto(False, photo)

window.title("Meta Scripts Youtube Converter")
window.geometry('350x200')

link_label = Label(window,text="Paste to YouTube Link")
link_label.pack(padx = 10,pady=2,anchor="w")

status_label = Label(window,text="Waiting...")
status_label.pack(padx = 10,pady=0,anchor="center")


link = Entry(window,width=70,fg='#7F7FFF')
link.pack(padx = 10,pady=1,anchor="w")


downloand_btn = Button(window,width=25,text="Download",command=click)
downloand_btn.pack(padx = 75,pady=10,anchor="w")


file_type = IntVar()

mp_3_check = Radiobutton(window,variable=file_type, value=1,text ="MP3")
mp_3_check.pack(padx = 125,pady=10,anchor="w")

file_type.set(1)


mp_4_check = Radiobutton(window,variable=file_type, value=2,text ="MP4")
mp_4_check.pack(padx = 125,pady=10,anchor="w")



window.mainloop()

