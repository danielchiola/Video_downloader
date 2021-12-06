from tkinter import *
import pytube
import youtube_dl

root = Tk()
root.geometry('800x600')
root.resizable(0,0)
root.title("Rayon video downloader")
Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

link = StringVar()
Label(root, text = 'Incolla qui il tuo link:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)
ydl_opts = {'nocheckcertificate': True,}
def Downloader():
    url =link.get()
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    Label(root, text = ' VIDEO SCARICATO', font = 'arial 15').place(x= 180 , y = 210)
Button(root,text = 'SCARICA VIDEO', font = 'arial 15 bold' ,bg = 'blue', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()