"""
Funcionalidad vista principal de votacion
"""

from tkinter import *

# abrir vista gobernacion
def show_gobernacion():
    try:
        from views import gob
    except ImportError:
        import sys
        gob = sys.modules[__package__ + '.gob']
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
