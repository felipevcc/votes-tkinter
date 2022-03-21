"""
Funcionalidad de vista votacion por alcaldia
"""

from tkinter import *
from tkinter import messagebox
from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from views import alc

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

# regresar a vista principal de votacion sin votar
def regresar():
    global boton_marcado
    boton_marcado = None
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']
    ventana = alc.v_alc
    ventana.destroy() 
    votacion.func_states(NORMAL,1)

# reiniciar variable de boton marcado y volver a la vista principal de votacion mediante la funcion terminar()
def terminar2():
    global boton_marcado
    boton_marcado = None
    try:
        import votacion
    except ImportError:
        import sys
        votacion = sys.modules[__package__ + '.votacion']
    votacion.func_states(DISABLED,1)

# Sumar voto (Boton de Finalizar) y establecer estado del boton
def terminar():
    voto = False
    try:
        for i in range(len(botones)):
            if boton_marcado == i:
                candidatos_alc[i][1]+=1
                voto = True
        try:
            import inicio
        except ImportError:
            import sys
            inicio = sys.modules[__package__ + '.inicio']
            inicio.acum_votos_alcaldia = candidatos_alc
            inicio.acum_lista_votantes[-1][2] = 'S'
    except:
        pass
    if voto == False:
        messagebox.showinfo(message="Debe votar, de lo contrario regrese atrás", title="ERROR")
    else:
        ventana = alc.v_alc
        ventana.destroy() 
        terminar2()