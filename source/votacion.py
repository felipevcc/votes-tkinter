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
