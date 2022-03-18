"""
Funcionalidad vista principal de votacion
"""

from tkinter import *

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
    try:
        from views import alc
    except ImportError:
        import sys
        alc = sys.modules[__package__ + '.alc']
    alc.alc()

# salir de votacion y abrir inicio
def show_inicio():
    try:
        from views import inicio
    except ImportError:
        import sys
        inicio = sys.modules[__package__ + '.inicio']
    inicio.inicio()

# estado de cada boton (gobernacion/alcaldia)
states = [NORMAL,NORMAL]
def func_states(state,posicion):
    states[posicion]=state
    vot.voting_section(states[0],states[1])