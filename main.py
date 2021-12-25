from math import pi
import speech_recognition as sr
import subprocess as sub
import pyttsx3 as voz
from time import sleep
from pynput import keyboard as kb

TeclaPared = "c";
TeclaSuelo = "x";
TeclaTecho = "v";
TeclaEscalera = "z";
    
def VerMenu():
    print("Si esta es la primera vez que entras, tendras que configurar tus teclas a continuación")
    print("1.- Modificar Teclas")
    print("2.- Restablecer Ajustes")
    print("3.- Ver Teclas")
    print("0.-Salir")
    OpcionPrincipal = int(input("Selecciona la opcion mas conveniente: "))
    if OpcionPrincipal == 1:
        ModificarTeclas()
    elif OpcionPrincipal == 2:
        RestablecerTeclas()
    elif OpcionPrincipal == 3:
        VerTeclas()
    else:
        Salir()
def ModificarTeclas():
    print("||||||||| Acontinuación toca la tecla con la que quieres construir las paredes. |||||||||")
    TeclaPared = str(input("Tecla Pared : "))
    print("Tecla Pared:")
    print(TeclaPared)
    print("  ")
    print("||||||||| Acontinuación toca la tecla con la que quieres construir los suelos. |||||||||")
    TeclaSuelo = str(input("Tecla Suelo : "))
    print("Tecla Suelo:")
    print(TeclaSuelo)
    print("  ")
    print("||||||||| Acontinuación toca la tecla con la que quieres construir los techos. |||||||||")
    TeclaTecho = str(input("Tecla Techo : "))
    print("Tecla Techo:")
    print(TeclaTecho)
    print("  ")
    print("||||||||| Acontinuación toca la tecla con la que quieres construir las Escaleras. |||||||||")
    TeclaEscalera = str(input("Tecla Escalera : "))
    print("Tecla Escalera:")
    print(TeclaEscalera)
    print("  ")
    print("Guardado Exitoso")
    print("Pulsa cualquier tecla para regresar al menu principal")
    OpcionTecla = str(input())   
    if OpcionTecla == 1:
        sub.call('clear', shell=True)
        VerMenu()
    else:
        sub.call('clear', shell=True)
        VerMenu()

def RestablecerTeclas():
    TeclaPared = "c";
    TeclaSuelo = "x";
    TeclaTecho = "v";
    TeclaEscalera = "z";
    print("Ajustes restablecidos con exito")
    print("")
    print("Pulsa cualquier tecla para regresar al menu principal")
    OpcionTecla = str(input())   
    if OpcionTecla == 1:
        sub.call('clear', shell=True)
        VerMenu()
    else:
        sub.call('clear', shell=True)
        VerMenu()


def pulsa(tecla):
    if tecla == kb.KeyCode.from_char('x'):
        print("Se ha construido Suelo x")
        print("Se ha activado tecla Suelo Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroSuelo.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('z'):
        print("Se ha construido Pared z")
        print("Se ha activado tecla Pared Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroPared.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('v'):
        print("Se ha construido Techo v")
        print("Se ha activado tecla Techo Infinitamente, para cancelar use Ctrl+Cq")
        sub.call('bash Macro/macroTecho.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('c'):
        print("Se ha construido Escalera c")
        print("Se ha activado tecla Escalera Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroEscalera.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('p'):
        print("Se ha activado tecla Usar Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroUsar.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('X'):
        print("Se ha construido Suelo X")
        print("Se ha activado tecla Suelo Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroSuelo.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('Z'):
        print("Se ha construido Pared Z")
        print("Se ha activado tecla Pared Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroPared.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('V'):
        print("Se ha construido Techo V")
        print("Se ha activado tecla Techo Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroTecho.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('C'):
        print("Se ha construido Escalera C")
        print("Se ha activado tecla Escalera Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroEscalera.sh', shell=True)
    elif tecla == kb.KeyCode.from_char('P'):
        print("Se ha activado tecla Usar Infinitamente, para cancelar use Ctrl+C")
        sub.call('bash Macro/macroUsar.sh', shell=True)
    
def VerTeclas():
    print("Tecla Pared:")
    print(TeclaPared)
    print("Tecla Suelo:")
    print(TeclaSuelo)
    print("Tecla Techo:")
    print(TeclaTecho)
    print("Tecla Escalera:")
    print(TeclaEscalera)
    print("Tecla Usar Infinitamente:")
    print("P")
    with kb.Listener(pulsa) as escuchador:
        escuchador.join()
        sleep(3q)
    #OpcionTecla = str(input())   
    #if OpcionTecla == 1:
    #    sub.call('clear', shell=True)
    #    VerMenu()
    #else:
    #    sub.call('clear', shell=True)
    #    VerMenu()

def Salir():
    sub.call('clear', shell=True)
    sub.call('exit', shell=True)

print("Iniciooooooooooooooooo") 
VerMenu()

def pulsa(tecla):
	print(str(tecla))
	with kb.Listener(pulsa) as escuchador:
	    escuchador.join()