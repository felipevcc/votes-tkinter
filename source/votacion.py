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
