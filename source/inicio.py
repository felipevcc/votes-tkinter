"""
Funcionalidad vista de inicio
"""

from tkinter import *

# conectar con vista de votacion y configurar el estado de los botones 
def show_votacion():
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']
    votacion.func_states(NORMAL,3)