"""import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from views.gob import gob"""

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

# Suma de votos
def suma(a):
    candidatos[a][1]+=1
    # aqui mismo se debe cerrar la votacion del usuario
    print(candidatos)
