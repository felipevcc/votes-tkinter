"""
Funcionalidad de vista votacion por gobernacion
"""

from tkinter import *
from tkinter import messagebox
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from views import gob

# Matriz candidatos y sus votos
def candidatos():
    opc_votos = [['Candidato 1', 0],
                ['Candidato 2', 0],
                ['Candidato 3', 0],
                ['Candidato 4', 0],
                ['Candidato 5', 0],
                ['Voto en blanco', 0]]
    return opc_votos
candidatos_gob = candidatos()

# Configuracion de botones al dar click
def config(a,b1,b2,b3,b4,b5,vb):
    global botones
    global boton_marcado

    botones = [b1,b2,b3,b4,b5,vb]
    boton_marcado = a
    for i in range(len(botones)):
        if a == i:
            botones[i].configure(bg='white')
        else:
            botones[i].configure(bg='grey')

# regresar a vista principal de votacion sin votar
def regresar():
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']
    votacion.func_states(NORMAL,0)

# reiniciar variable de boton marcado y volver a la vista principal de votacion mediante la funcion terminar()
def terminar2():
    global boton_marcado
    boton_marcado = None
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']
    votacion.func_states(DISABLED,0)

# sumar voto (Boton de Finalizar) y establecer estado del boton
def terminar():
    voto = False
    try:
        for i in range(len(botones)):
            if boton_marcado == i:
                candidatos_gob[i][1]+=1
                voto = True
                print(candidatos_gob)
    except: 
        pass
    if voto == False:
        messagebox.showinfo(message="Debe votar, de lo contrario regrese atrás", title="ERROR")
    else:
        ventana = gob.v_gob
        ventana.destroy() 
        terminar2()
