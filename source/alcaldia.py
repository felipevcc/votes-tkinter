"""
Funcionalidad de vista votacion por alcaldia
"""

from tkinter import *

# Matriz candidatos y sus votos
def candidatos():
    opc_votos = [['Candidato 1', 0],
                ['Candidato 2', 0],
                ['Candidato 3', 0],
                ['Candidato 4', 0],
                ['Candidato 5', 0],
                ['Voto en blanco', 0]]
    return opc_votos
candidatos_alc = candidatos()

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

# Sumar voto (Boton de Finalizar) y establecer estado del boton
def terminar():
    for i in range(len(botones)):
        if boton_marcado == i:
            candidatos_alc[i][1]+=1
            print(candidatos_alc)
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']
    votacion.func_states(DISABLED,1)