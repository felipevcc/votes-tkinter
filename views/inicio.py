"""
Vista de inicio
"""

from tkinter import *
from .vot import *

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from source.inicio import *

def inicio():

    # ------------ window -----------
    
    inicio = Tk()
    inicio.title('Inicio')
    inicio.configure(bg='white')

    ancho_ventana = 750
    alto_ventana  = 550

    x_ventana = inicio.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = inicio.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    inicio.geometry(posicion)

    # --------- connections ----------

    def s_votacion():
        inicio.destroy()
        show_votacion()
        
    # ---------- Headboard -----------

    # img elecciones 2022
    img1 = PhotoImage(master=inicio, file='img/elecciones2.png')
    lbl_img1 = Label(inicio, image=img1, bg='white')

    h1 = Label(inicio, text='ELECCIONES CALI 2022', bg='white', font=('helvetica', 14))


    # ---------- buttons ------------



    votar = Button(inicio, text='VOTAR', command=s_votacion)

    # ----- llamados y ubicaciones -----

    h1.pack()
    h1.place(x=270, y=40)

    lbl_img1.pack()
    lbl_img1.place(x=90, y=7)

    votar.pack()
    inicio.mainloop()
