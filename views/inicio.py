"""
Vista de inicio
"""

from cgitb import text
from tkinter import *
from .vot import *

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from source.inicio import *
from source.resultado import *


PASS_ADMIN = 'admin123'

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
        cedula_votante = txt_cedula_identidad.get()
        sexo_votante   = opcion.get()
        txt_cedula_identidad.delete(0,END)
        if validar_votante(cedula_votante, sexo_votante):
            inicio.destroy()
            show_votacion(cedula_votante, sexo_votante)
        opcion.set(0)

         
    #Definir popup para validar password de administrador
    def popup():
        se_puede_cerrar = False
        try:
            se_puede_cerrar = validar_almenos_1_voto()
        except:
            pass

        if se_puede_cerrar:

            top = Tk()
            top.title('Opciones de Administrador')
            top.configure(bg='white')
            ancho_ventana = 400
            alto_ventana  = 60

            x_ventana = top.winfo_screenwidth() // 2 - ancho_ventana // 2
            y_ventana = top.winfo_screenheight() // 2 - alto_ventana // 2

            posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
            top.geometry(posicion)

            entry = Entry(top, width= 30)
            entry.config(show='*')
            entry.pack()

            def s_resultado():            
                inicio.destroy()
                show_resultado()

            def validar():            
                if entry.get() == PASS_ADMIN:
                    top.destroy()
                    s_resultado()
                else:
                    messagebox.showinfo(message="La contraseña de administrador ingresada es incorrecta", title="ERROR")
                    top.destroy()

            Button(top,text= "Validar Permisos", command= validar).pack(pady= 5,side=TOP)
        else:
            messagebox.showinfo(message="La maquina no se puede cerrar, debe haber al menos 1 voto para gobernación y 1 voto para alcaldía, diferente de Voto en Blanco", title="ERROR")

    # ---------- Headboard -----------

    # img elecciones 2022
    img1 = PhotoImage(master=inicio, file='img/elecciones2.png')
    lbl_img1 = Label(inicio, image=img1, bg='white')

    h1 = Label(inicio, text='ELECCIONES CALI 2022', bg='white', font=('helvetica', 14))

    # ---------- Entrys ------------
    lbl_cedula_identidad = Label(inicio, text='Ingrese su número de cédula : ', font=('helvetica', 12), bg='white')
    txt_cedula_identidad = Entry(inicio, width=50, font=('helvetica', 10))
    
    # ---------- RadioButtons ------------
    opcion = IntVar()
    lbl_seleccion_sexo = Label(inicio, text='Seleccione su género : ', font=('helvetica', 12), bg='white')
    rbt_masculino = Radiobutton(inicio, text='Masculino', variable=opcion, value=1)
    rbt_femenino  = Radiobutton(inicio, text='Femenino',  variable=opcion, value=2)

    # ---------- buttons ------------
    btn_votar = Button(inicio, text='Iniciar Votación', command=s_votacion)
    btn_cerrar_caja = Button(inicio, text='Cerrar mesa', command=popup, font=('helvetica', 12))

    # ----- llamados y ubicaciones -----

    h1.pack()
    h1.place(x=270, y=40)

    lbl_img1.pack()
    lbl_img1.place(x=90, y=7)

    btn_cerrar_caja.pack()
    btn_cerrar_caja.place(x=600, y=40)

    lbl_cedula_identidad.pack()
    lbl_cedula_identidad.place(x=100, y=240)
    txt_cedula_identidad.pack()
    txt_cedula_identidad.place(x=100, y= 270)

    lbl_seleccion_sexo.pack()
    lbl_seleccion_sexo.place(x=500, y=240)
    rbt_masculino.pack()
    rbt_masculino.place(x=500, y=270)
    rbt_femenino.pack()
    rbt_femenino.place(x=600, y=270)

    btn_votar.pack()
    btn_votar.place(x=100, y=300)
    inicio.mainloop()
