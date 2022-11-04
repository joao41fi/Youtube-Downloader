

from pytube import *
from pytube.cli import on_progress
from tkinter import * 
from tkinter.ttk import *
from tkinter import filedialog 
import _thread
import progressbar as progress
import os    


global pasta
u_name = os.getlogin()
print(f"[*] Username is : {u_name}")
pastas = str('C:/Users/'+u_name+'/Downloads')
print(pastas)


def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = ys.filesize
    size = contentsize - bytes_remaining

    #print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    #'█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
    #print(size,bytes_remaining,contentsize)   #contentsize == 100
    progresse['value'] = size/contentsize*100
    ferame.update_idletasks()
    return print(size,bytes_remaining,contentsize) 
                                              



def baixas(link):
    global ys
   
    
    yt  = YouTube(link, on_progress_callback= progress)
    
    ys = yt.streams.get_highest_resolution()
    ys.download(pastas)
   
def ok():
    link = biaxa.get()
    progresse['value'] = 0
    try:
     _thread.start_new_thread(baixas, (link,))
    except Exception:
     print
    
def pasta ():
 global pastas 
 pastas = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 

janela = janela = Tk()
win_width, win_height = 200, 200
janela.geometry(f'{win_width}x{win_height}')

ferame = Frame(janela)
ferame.pack()

progresse = Progressbar(janela, orient = HORIZONTAL, length = 100)

progresse.place(x=20,y=110)

  

avisos = Label(janela,text='link do vidio')
avisos.place(x=20,y=30)
biaxa = Entry(janela)

biaxa.place(x=20,y=50)

bot= Button(janela,text="procura",command = lambda:pasta()) 
bot.place(x=110,y=80)

bot= Button(janela,text="Baixa",command = lambda:ok()) 
bot.place(x=30,y=80)
janela.mainloop()

  





