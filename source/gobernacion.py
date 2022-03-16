from tkinter import *

"""import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )"""

"""import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))"""


"""from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))"""

#from views.gob import *

# Matriz candidatos y sus votos
def candidatos():
    opc_votos = [['Candidato 1', 0],
                ['Candidato 2', 0],
                ['Candidato 3', 0],
                ['Candidato 4', 0],
                ['Candidato 5', 0],
                ['Voto en blanco', 0]]
    return opc_votos
candidatos = candidatos()

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

# Sumar voto (Boton de Finalizar)
def terminar():
    for i in range(len(botones)):
        if boton_marcado == i:
            candidatos[i][1]+=1
            print(candidatos)
        #Aqui debe retroceder a la vista anterior


