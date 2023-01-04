from pytube import *

from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog 
import _thread
import progressbar as progress
import os    
from tkinter import ttk
import threading

global pasta
u_name = os.getlogin()
print(f"[*] Username is : {u_name}")
pastas = str('C:/Users/'+u_name+'/Downloads')
print(pastas)


class baixar (): 
 def __init__(self):
  self.janela()
   
 def pasta (self):
  global pastas 
  pastas = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH") 

 def link_viu(self,num):
  while True:
   linke = self.biaxa.get()
   if linke != '':
     try : 
      yt = YouTube(linke)
      print('e vidio')
      lista_resul = self.lista_resulusão(yt)
      print(lista_resul)
      
      
      self.month_cb['values'] = lista_resul
      self.month_cb.current(5) 
      
     except Exception:
      print('Não e vidio')
     print(linke)
    
    
 def lista_resulusão(self,yt): 
  

  videos = yt.streams

  lista_resul = []

  for i in range(len(videos)):
    #print(i,videos[i])
    ok= videos[i]
    ok = str(ok)
    ok =ok.split(None)
    lista_resul.append(ok[3])

  #print(lista_resul)
  lista_resul_fin = []
  for i in lista_resul:
   lista_resul_fin.append( i[4:])
 
  return lista_resul_fin 

 def progress(self,streams, chunk: bytes, bytes_remaining: int):
    contentsize = ys.filesize
    size = contentsize - bytes_remaining

    #print('\r' + '[Download progress]:[%s%s]%.2f%%;' % 
    #'█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')
    #print(size,bytes_remaining,contentsize)   #contentsize == 100
    self.progresse['value'] = size/contentsize*100
    self.ferame.update_idletasks()
    return print(size,bytes_remaining,contentsize) 


 def baixas(self,link):
    global ys
   
    yt  = YouTube(link, on_progress_callback= self.progress)
    
    ys = yt.streams.get_highest_resolution()
    ys.download(pastas)
   

 def start_teding(self):
    link = self.biaxa.get()
    self.progresse['value'] = 0
    try:
     _thread.start_new_thread(self.baixas, (link,))
    except Exception:
     print
   
    

 def janela(self):
  janela = janela = Tk()
  win_width, win_height = 200, 200
  janela.geometry(f'{win_width}x{win_height}')

  self.ferame = Frame(janela)
  self.ferame.pack()

  self.progresse = Progressbar(janela, orient = HORIZONTAL, length = 100)

  self.progresse.place(x=20,y=110)

  

  avisos = Label(janela,text='link do vidio')
  avisos.place(x=20,y=30)
  self.biaxa = Entry(janela)

  self.biaxa.place(x=20,y=50)

  bot= Button(janela,text="procura",command = lambda: self.pasta()) 
  bot.place(x=110,y=80)

  bot= Button(janela,text="Baixa",command = lambda:self.start_teding()) 
  bot.place(x=30,y=80)

  label = ttk.Label( janela ,text="Please select a month:")
  label.place(x=50,y=135)


  self.month_cb = ttk.Combobox(janela)





  try:
   self.month_cb.current(5) 
  except :
   print
  
  self.month_cb.place(x=50,y=155)
  try:
   _thread.start_new_thread(self.link_viu, (1,))
  except:
    print
  janela.mainloop()


baixar()