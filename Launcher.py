from tkinter import *
from tkinter.ttk import *
import jeu
import credits
import pickle
import os
fen1=Tk()

fen1.title("Dragon Bowble")
fen1.geometry("850x532")
Fond=Canvas(fen1,width=850,height=532,bg='white')
fichier=PhotoImage(file='picture/logo.gif')
Fond.create_image(425,266,image=fichier)
Fond.place(x=0,y=0)
bou1=Button(fen1, text="Jouer", command=jeu.lancer_jeu)
bou1.pack()
bou1.place(relx=0.45, rely=0.96, anchor=CENTER)

bou2=Button(fen1, text="Quitter", command=fen1.destroy)
bou2.pack()
bou2.place(relx=0.55, rely=0.96, anchor=CENTER)



menubar = Menu(fen1)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=fen1.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)

fen1.config(menu=menubar)
os.startfile('help.html')

fen1.mainloop()
