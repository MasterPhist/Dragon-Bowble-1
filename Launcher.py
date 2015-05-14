from tkinter import *
import jeu
import credits
fen1=Tk()

fen1.title("Dragon Bowble")
fen1.geometry("850x532")
Fond=Canvas(fen1,width=850,height=532,bg='white')
fichier=PhotoImage(file='picture/logo.gif')
Fond.create_image(425,266,image=fichier)
Fond.place(x=0,y=0)
bou1=Button(fen1, text="Jouer", command=jeu.lancer_jeu)
bou1.pack()
bou1.place(relx=0.4, rely=0.96, anchor=CENTER)

bou2=Button(fen1, text="Quitter", command=fen1.destroy)
bou2.pack()
bou2.place(relx=0.5, rely=0.96, anchor=CENTER)

bou3=Button(fen1, text="Highscore", command=fen1.destroy)
bou3.pack()
bou3.place(relx=0.6, rely=0.96, anchor=CENTER)

menubar = Menu(fen1)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=fen1.destroy)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="À propos", command=credits.credits)
menubar.add_cascade(label="Aide", menu=menu2)

fen1.config(menu=menubar)

fen1.mainloop()