"""
Vista de resultado
"""

from tkinter import *

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from source import resultado


def result_section():
    

    candidato_ganador_alcalde    = resultado.candidato_ganador_alcaldia()
    candidato_ganador_gobernador = resultado.candidato_ganador_gobernacion()

    nombre_candidato_alcalde = candidato_ganador_alcalde[0]
    cantidad_votos_candidato_alcalde = candidato_ganador_alcalde[1]

    nombre_candidato_gobernador = candidato_ganador_gobernador[0]
    cantidad_votos_candidato_gobernador = candidato_ganador_gobernador[1]

    cantidad_votos_blanco_gobernacion = resultado.contar_votos_blanco_gobernacion()
    cantidad_votos_blanco_alcaldia = resultado.contar_votos_blanco_alcaldia()

    cantidad_total_votos_gobernacion = resultado.contar_cantidad_total_votos_gobernacion()
    cantidad_total_votos_alcaldia = resultado.contar_cantidad_total_votos_alcaldia()

    cantidad_total_hombres_gobernacion = resultado.contar_total_hombres_votantes_gobernacion()
    cantidad_total_mujeres_gobernacion = resultado.contar_total_mujeres_votantes_gobernacion()

    cantidad_total_hombres_alcaldia = resultado.contar_total_hombres_votantes_alcaldia()
    cantidad_total_mujeres_alcaldia = resultado.contar_total_mujeres_votantes_alcaldia()

    porcentaje_votos_hombre_gobernacion = (cantidad_total_hombres_gobernacion*100) / cantidad_total_votos_gobernacion
    porcentaje_votos_mujeres_gobernacion = (cantidad_total_mujeres_gobernacion*100) / cantidad_total_votos_gobernacion

    porcentaje_votos_hombre_alcaldia = (cantidad_total_hombres_alcaldia*100) / cantidad_total_votos_alcaldia
    porcentaje_votos_mujeres_alcaldia = (cantidad_total_mujeres_alcaldia*100) / cantidad_total_votos_alcaldia

    
    # ------------ window -----------
    global v_resultado
    v_resultado = Tk()
    v_resultado.title('Resultados')
    v_resultado.configure(bg='white')
    v_resultado.resizable(0,0)

    ancho_ventana = 750
    alto_ventana  = 550

    x_ventana = v_resultado.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = v_resultado.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    v_resultado.geometry(posicion)

    # ---------- Headboard -----------
    def finalizar_votacion():
        v_resultado.destroy()

    # img elecciones 2022
    img1 = PhotoImage(master=v_resultado, file='img/elecciones2.png')
    lbl_img1 = Label(v_resultado, image=img1, bg='white')

    h1 = Label(v_resultado, text='ELECCIONES CALI 2022', bg='white', font=('helvetica', 14))


    # --------- Mostrar Resultados ---------
    img_candidato = PhotoImage(master=v_resultado, file='img/candidato.png')
    img_gobernacion2 = PhotoImage(master=v_resultado, file='img/gobernacion2.png')
    img_alcaldia2 = PhotoImage(master=v_resultado, file='img/alcaldia2.png')
    
    lbl_titulo1 = Label(v_resultado, image=img_gobernacion2, bg='white')
    lbl_ganador_gobernador = Label(v_resultado, image=img_candidato, bg='white')
    lbl_nombre_cantidato_gobernador = Label(v_resultado, text='Ganador : ' + nombre_candidato_gobernador, bg='white', font=('helvetica', 10))
    lbl_votos_cantidato_gobernador = Label(v_resultado, text='Votos Candidato : '+str(cantidad_votos_candidato_gobernador), bg='white', font=('helvetica', 10))
    lbl_votos_blanco_gobernacion = Label(v_resultado, text='Total Votos en Blanco : ' + str(cantidad_votos_blanco_gobernacion), bg='white', font=('helvetica', 10))    
    lbl_total_votos_gobernacion = Label(v_resultado, text='Cantidad Total Votos : ' + str(cantidad_total_votos_gobernacion), bg='white', font=('helvetica', 10))    
    lbl_total_votos_hombres_gobernacion = Label(v_resultado, text='Cantidad Votos Hombres : ' + str(cantidad_total_hombres_gobernacion), bg='white', font=('helvetica', 10))    
    lbl_total_votos_mujeres_gobernacion = Label(v_resultado, text='Cantidad Votos Mujeres : ' + str(cantidad_total_mujeres_gobernacion), bg='white', font=('helvetica', 10))    
    lbl_porcentaje_votos_hombres_gobernacion = Label(v_resultado, text='Porcentaje Votos Hombres : ' + str(round(porcentaje_votos_hombre_gobernacion,2)) + '%', bg='white', font=('helvetica', 10))    
    lbl_porcentaje_votos_mujeres_gobernacion = Label(v_resultado, text='Porcentaje Votos Mujeres : ' + str(round(porcentaje_votos_mujeres_gobernacion,2)) + '%', bg='white', font=('helvetica', 10))    

    lbl_titulo2 = Label(v_resultado, image=img_alcaldia2, bg='white')
    lbl_ganador_alcaldia = Label(v_resultado, image=img_candidato, bg='white')
    lbl_nombre_cantidato_alcaldia = Label(v_resultado, text='Ganador : ' + nombre_candidato_alcalde, bg='white', font=('helvetica', 10))
    lbl_votos_cantidato_alcaldia = Label(v_resultado, text='Votos Candidato : '+str(cantidad_votos_candidato_alcalde), bg='white', font=('helvetica', 10))
    lbl_votos_blanco_alcaldia = Label(v_resultado, text='Total Votos en Blanco : ' + str(cantidad_votos_blanco_alcaldia), bg='white', font=('helvetica', 10))
    lbl_total_votos_alcaldia = Label(v_resultado, text='Cantidad Total Votos : ' + str(cantidad_total_votos_alcaldia), bg='white', font=('helvetica', 10))
    lbl_total_votos_hombres_alcaldia = Label(v_resultado, text='Cantidad Votos Hombres : ' + str(cantidad_total_hombres_alcaldia), bg='white', font=('helvetica', 10))    
    lbl_total_votos_mujeres_alcaldia = Label(v_resultado, text='Cantidad Votos Mujeres : ' + str(cantidad_total_mujeres_alcaldia), bg='white', font=('helvetica', 10))
    lbl_porcentaje_votos_hombres_alcaldia = Label(v_resultado, text='Porcentaje Votos Hombres : ' + str(round(porcentaje_votos_hombre_alcaldia,2)) + '%', bg='white', font=('helvetica', 10))    
    lbl_porcentaje_votos_mujeres_alcaldia = Label(v_resultado, text='Porcentaje Votos Mujeres : ' + str(round(porcentaje_votos_mujeres_alcaldia,2)) + '%', bg='white', font=('helvetica', 10))    
    
    btn_cerrar_votacion = Button(v_resultado, text='Cerrar Proceso Votación', bg='white', font=('helvetica', 10), command=finalizar_votacion)

    # ----- llamados y ubicaciones -----

    h1.pack()
    h1.place(x=270, y=40)

    lbl_img1.pack()
    lbl_img1.place(x=90, y=7)

    lbl_titulo1.pack()
    lbl_titulo1.place(x=90, y=100)
    lbl_ganador_gobernador.pack()
    lbl_ganador_gobernador.place(x=90, y=230)
    lbl_nombre_cantidato_gobernador.pack()
    lbl_nombre_cantidato_gobernador.place(x=90, y=340)
    lbl_votos_cantidato_gobernador.pack()
    lbl_votos_cantidato_gobernador.place(x=90, y=360)
    lbl_votos_blanco_gobernacion.pack()
    lbl_votos_blanco_gobernacion.place(x=90, y=380)
    lbl_total_votos_gobernacion.pack()
    lbl_total_votos_gobernacion.place(x=90, y=400)
    lbl_total_votos_hombres_gobernacion.pack()
    lbl_total_votos_hombres_gobernacion.place(x=90, y=420)
    lbl_total_votos_mujeres_gobernacion.pack()
    lbl_total_votos_mujeres_gobernacion.place(x=90, y=440)
    lbl_porcentaje_votos_hombres_gobernacion.pack()
    lbl_porcentaje_votos_hombres_gobernacion.place(x=90, y=460)
    lbl_porcentaje_votos_mujeres_gobernacion.pack()
    lbl_porcentaje_votos_mujeres_gobernacion.place(x=90, y=480)

    lbl_titulo2.pack()
    lbl_titulo2.place(x=470, y=100)
    lbl_ganador_alcaldia.pack()
    lbl_ganador_alcaldia.place(x=470, y=230)
    lbl_nombre_cantidato_alcaldia.pack()
    lbl_nombre_cantidato_alcaldia.place(x=470, y=340)
    lbl_votos_cantidato_alcaldia.pack()
    lbl_votos_cantidato_alcaldia.place(x=470, y=360)
    lbl_votos_blanco_alcaldia.pack()
    lbl_votos_blanco_alcaldia.place(x=470, y=380)
    lbl_total_votos_alcaldia.pack()
    lbl_total_votos_alcaldia.place(x=470, y=400)
    lbl_total_votos_hombres_alcaldia.pack()
    lbl_total_votos_hombres_alcaldia.place(x=470, y=420)
    lbl_total_votos_mujeres_alcaldia.pack()
    lbl_total_votos_mujeres_alcaldia.place(x=470, y=440)
    lbl_porcentaje_votos_hombres_alcaldia.pack()
    lbl_porcentaje_votos_hombres_alcaldia.place(x=470, y=460)
    lbl_porcentaje_votos_mujeres_alcaldia.pack()
    lbl_porcentaje_votos_mujeres_alcaldia.place(x=470, y=480)

    btn_cerrar_votacion.pack()
    btn_cerrar_votacion.place(x=550, y=40)

    v_resultado.mainloop()