"""
Funcionalidad vista principal de votacion
"""

from tkinter import *
from tkinter import messagebox

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from views import vot

# abrir vista gobernacion
def show_gobernacion():
    votacion = vot.votacion
    try:
        from views import gob
    except ImportError:
        import sys
        gob = sys.modules[__package__ + '.gob']
    votacion.destroy()
    gob.gob()

# abrir vista alcaldia
def show_alcaldia():
    votacion = vot.votacion
    try:
        from views import alc
    except ImportError:
        import sys
        alc = sys.modules[__package__ + '.alc']
    votacion.destroy()
    alc.alc()

#estado de los botones
states = [NORMAL,NORMAL]

# salir a la vista de inicio y verificar si se voto por al menos una corporacion
def show_inicio():
    try:
        from views import inicio
    except ImportError:
        import sys
        inicio = sys.modules[__package__ + '.inicio']
    ventana = vot.votacion
    if states[0] == NORMAL and states[1] == NORMAL:
        messagebox.showinfo(message="Debe votar al menos por una corporación", title="ERROR")
    else:
        ventana.destroy()
        inicio.inicio()

# estado de cada boton (gobernacion/alcaldia)
def func_states(state,posicion):
    if posicion == 3:
        states[0]=state
        states[1]=state
    else:
        states[posicion]=state
    vot.voting_section(states[0],states[1])