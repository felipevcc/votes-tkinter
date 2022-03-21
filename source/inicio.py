"""
Funcionalidad vista de inicio
"""

from tkinter import *
from tkinter import messagebox

acum_lista_votantes     = []
acum_votos_alcaldia     = []
acum_votos_gobernacion  = []


def validar_almenos_1_voto():

    se_puede_cerrar = False
    for i in range(len(acum_votos_alcaldia[:4])):
        if acum_votos_alcaldia[i][1]>0:
            se_puede_cerrar = True
    
    se_puede_cerrar2 = False
    for i in range(len(acum_votos_gobernacion[:4])):
        if acum_votos_gobernacion[i][1]>0:
            se_puede_cerrar2 = True

    if se_puede_cerrar and se_puede_cerrar2:
        return True
    else:
        return False
    

# validar si el votante ya ejercio su voto
def validar_votante(cedula, sexo):
        
    for i in range(len(acum_lista_votantes)):
        if cedula in acum_lista_votantes[i][0]:
            messagebox.showinfo(message="El documento ingresado ya se encuentra registrado, tenga en cuenta que solo puede votar 1 vez", title="ERROR")
            return False

    try:
        int(cedula)
    except ValueError:
        messagebox.showinfo(message="El documento ingresado no es valido", title="ERROR")
        return False

    if len(cedula)<7:
        messagebox.showinfo(message="El documento ingresado no es valido", title="ERROR")
        return False
    
    if sexo==0:
        messagebox.showinfo(message="Debe seleccionar su sexo", title="ERROR")
        return False
    
    return True

    

# conectar con vista de votacion y configurar el estado de los botones 
def show_votacion(cedula_votante, sexo_votante):
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']
    
    acum_lista_votantes.append([cedula_votante,sexo_votante,'N','N'])
    votacion.func_states(NORMAL,3)

