"""
Vista principal de votacion
"""

from tkinter import *

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from source.votacion import *

def voting_section(state_gob, state_alc):

    # ------------ window -----------
    global votacion
    votacion = Tk()
    votacion.geometry('750x550')
    votacion.title('Elecciones Cali 2022')
    votacion.configure(bg='white')

    # --------- connections ----------
    
    # conectar vista votacion por gobernacion
    def s_gob():
        show_gobernacion()
    
    # conectar vista votacion por alcaldia
    def s_alc():
        show_alcaldia()

    # conectar vista de inicio
    def salida():
        show_inicio()
    
    # ---------- Headboard -----------

    # img elecciones 2022
    img1 = PhotoImage(master=votacion, file='img/elecciones2.png')
    lbl_img1 = Label(votacion, image=img1, bg='white')

    h1 = Label(votacion, text='ELECCIONES CALI 2022', bg='white', font=('helvetica', 14))

    # ---------- buttons ------------
    img_gob = PhotoImage(master=votacion, file="img/gobernacion.png")
    gobernacion = Button(votacion, image=img_gob, relief="raised", borderwidth=2, command=s_gob, state=state_gob)

    img_alc = PhotoImage(master=votacion, file="img/alcaldia.png")
    alcaldia = Button(votacion, image=img_alc, relief="raised", borderwidth=2, command=s_alc, state=state_alc)
    
    # img registraduria
    img2 = PhotoImage(master=votacion, file='img/registraduria.png')
    lbl_img2 = Label(votacion, image=img2, bg='white')

    img_salir = PhotoImage(master=votacion, file="img/vote.png")
    salir = Button(votacion, text='Finalizar', font=('helvetica',12), image=img_salir, compound=RIGHT, command=salida)

    # ----- llamados y ubicaciones -----

    h1.pack()
    h1.place(x=270, y=55)

    lbl_img1.pack()
    lbl_img1.place(x=90, y=18)

    gobernacion.pack()
    gobernacion.place(x=75, y=125)

    alcaldia.pack()
    alcaldia.place(x=395, y=125)

    lbl_img2.pack()
    lbl_img2.place(x=562, y=450)

    salir.pack()
    salir.place(x=311, y=460)

    votacion.mainloop()
