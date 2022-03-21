"""
Funcionalidad vista resultado de votacion
"""

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from views import v_resultado

try:
    import inicio
except ImportError:
    import sys
    inicio = sys.modules[__package__ + '.inicio']


def show_resultado():
    v_resultado.result_section()

def candidato_ganador_alcaldia():
    ganador_alcaldia    = max(inicio.acum_votos_alcaldia[:4], key=lambda item:item[1])
    return ganador_alcaldia

def candidato_ganador_gobernacion():
    ganador_gobernacion    = max(inicio.acum_votos_gobernacion[:4], key=lambda item:item[1])
    return ganador_gobernacion

def contar_votos_blanco_alcaldia():
    cantidad_votos_blanco = inicio.acum_votos_alcaldia[-1][1]
    return cantidad_votos_blanco

def contar_votos_blanco_gobernacion():
    cantidad_votos_blanco = inicio.acum_votos_gobernacion[-1][1]
    return cantidad_votos_blanco

def contar_cantidad_total_votos_alcaldia():
    cantidad_total_votos_alcaldia = 0

    for i in range(len(inicio.acum_lista_votantes)):
        if inicio.acum_lista_votantes[i-1][2] == 'S':
            cantidad_total_votos_alcaldia += 1

    return cantidad_total_votos_alcaldia

def contar_cantidad_total_votos_gobernacion():
    cantidad_total_votos_gobernacion = 0
    
    for x in range(len(inicio.acum_lista_votantes)):
        if inicio.acum_lista_votantes[x-1][3] == 'S':
            cantidad_total_votos_gobernacion += 1

    return cantidad_total_votos_gobernacion

def contar_total_hombres_votantes_gobernacion():
    cantidad_total_hombres = 0
    for i in range(len(inicio.acum_lista_votantes)):
        if inicio.acum_lista_votantes[i-1][1] == 1 and inicio.acum_lista_votantes[i-1][3] == 'S' :
            cantidad_total_hombres += 1

    return cantidad_total_hombres

def contar_total_mujeres_votantes_gobernacion():
    cantidad_total_mujeres = 0
    for i in range(len(inicio.acum_lista_votantes)):
        if inicio.acum_lista_votantes[i-1][1] == 2 and inicio.acum_lista_votantes[i-1][3] == 'S' :
            cantidad_total_mujeres += 1

    return cantidad_total_mujeres


def contar_total_hombres_votantes_alcaldia():
    cantidad_total_hombres = 0
    for i in range(len(inicio.acum_lista_votantes)):
        if inicio.acum_lista_votantes[i-1][1] == 1 and inicio.acum_lista_votantes[i-1][2] == 'S':
            cantidad_total_hombres += 1

    return cantidad_total_hombres

def contar_total_mujeres_votantes_alcaldia():
    cantidad_total_mujeres = 0
    for i in range(len(inicio.acum_lista_votantes)):
        if inicio.acum_lista_votantes[i-1][1] == 2 and inicio.acum_lista_votantes[i-1][2] == 'S':
            cantidad_total_mujeres += 1

    return cantidad_total_mujeres