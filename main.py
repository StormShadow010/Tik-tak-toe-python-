from Funciones.Jugador.player import jugada
from Funciones.Jugador.player2 import jugada2
from Funciones.Jugador.ganadorplayer import ganaplayer
from Funciones.Jugador.ganaplayer2 import ganaplayer2
from Funciones.Inicio.stargame import impresioinicio
from Funciones.Maquina.machine import computador
from Funciones.Maquina.ganadormaquina import ganamaquina
from Funciones.Matriz.resultmatriz import impresionnueva
from Funciones.Matriz.empate import buscarempate
from Funciones.Resultados.impresionresultados import  impresionderesultados
from Funciones.Resultados.resultadomultiplayer import impresionderesultadosmulti


#Variables control
ganadasuser = 0
ganada2player=0
ganada1player=0
ganadacompu = 0
empate = 0
player=False
#Inicio
name=str(input("Digite su nombre:"))
print(f"Hola Bienvenido {name}")

Partida=str(input("Desea jugar triki:(S) para si y (N) para no:"))
if Partida=="S" or Partida=="s":
    while Partida == "S" or Partida=="s":
            R = int(input("Ingrese el numero de filas del tablero:"))
            print("\nTablero Inicial:")
            matriz=impresioinicio(R)
            multi=str(input("¿Desea jugar con la maquina o con otra persona? (M) para multiplayer o (A) para jugar con la maquina:"))
            if multi=="M" or multi=="m":

                if player==False:
                    name2=str(input("Digite el nombre del segundo jugador:"))
                player = True
                choose = str(input(f"¿Quien empieza jugando? (1) para {name} y (2) para {name2}:"))
                ganador = False
                if choose == "1":
                    print(f"-- Inicia jugando {name}  !!\n")
                    while ganador == False:
                        #Jugador 1
                        print(f"-- En su turno {name} !!")
                        matriz = jugada(R, matriz)
                        print("!! Tablero actualizado !!\n")
                        impresionnueva(R, matriz)
                        # Evaluar si gano el jugador 1
                        ganador, ganada1player, ganada2player, empate = ganaplayer(R, matriz, ganada1player, ganada2player,
                                                                               empate)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name,name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        # Resivar el empate
                        ganador, empate = buscarempate(R, matriz, empate)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name, name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        #Jugador 2
                        print(f"-- En su turno {name2} !!")
                        matriz = jugada2(R, matriz)
                        print("!! Tablero actualizado !!\n")
                        impresionnueva(R, matriz)
                        # Evaluar si gano el jugador 2
                        ganador, ganada1player, ganada2player, empate = ganaplayer2(R, matriz, ganada1player, ganada2player,
                                                                                empate,name2)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name,name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        # Resivar el empate
                        ganador, empate = buscarempate(R, matriz, empate)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name,name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                else:
                    print(f"-- Inicia jugando {name2}  !!\n")
                    while ganador == False:
                        # Jugador 2
                        print(f"-- En su turno {name2} !!")
                        matriz = jugada2(R, matriz)
                        print("!! Tablero actualizado !!\n")
                        impresionnueva(R, matriz)
                        # Evaluar si gano el jugador 2
                        ganador, ganada1player, ganada2player, empate = ganaplayer2(R, matriz, ganada1player, ganada2player,
                                                                                empate, name2)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name, name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        # Resivar el empate
                        ganador, empate = buscarempate(R, matriz, empate)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name, name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        # Jugador 1
                        print(f"-- En su turno {name} !!")
                        matriz = jugada(R, matriz)
                        print("!! Tablero actualizado !!\n")
                        impresionnueva(R, matriz)
                        # Evaluar si gano el jugador 1
                        ganador, ganada1player, ganada2player, empate = ganaplayer(R, matriz, ganada1player, ganada2player,
                                                                               empate)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name, name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        # Resivar el empate
                        ganador, empate = buscarempate(R, matriz, empate)
                        if ganador == True:
                            impresionderesultadosmulti(ganada1player, ganada2player, empate, name, name2)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
            else:
                choose = str(input("¿Desea que la maquina juegue primero? (S) para si y (N) para no:"))
                ganador = False
                if choose=="S" or choose=="s":
                     print("-- Inicia jugando la maquina !!\n")
                     while ganador==False:
                         matriz=computador(R,matriz)
                         print("!! Tablero actualizado !!\n")
                         impresionnueva(R, matriz)
                         # Evaluar si gano la maquina
                         ganador,ganadasuser,ganadacompu,empate=ganamaquina(R, matriz,ganadasuser,ganadacompu,empate)
                         if ganador==True:
                             impresionderesultados(ganadasuser, ganadacompu, empate, name)
                             Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                             break
                         print(f"-- En su turno {name} !!")
                         matriz = jugada(R, matriz)
                         print("!! Tablero actualizado !!\n")
                         impresionnueva(R,matriz)
                         # Evaluar si gano el jugador
                         ganador,ganadasuser,ganadacompu,empate=ganaplayer(R, matriz,ganadasuser,ganadacompu,empate)
                         if ganador == True:
                             impresionderesultados(ganadasuser,ganadacompu,empate,name)
                             Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                             break
                         # Resivar el empate
                         ganador,empate=buscarempate(R,matriz,empate)
                         if ganador==True:
                             impresionderesultados(ganadasuser, ganadacompu, empate, name)
                             Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                             break
                else:
                    print(f"-- Inicia jugando {name} !!")
                    while ganador == False:
                        print(f"En su turno {name}")
                        matriz=jugada(R,matriz)
                        print("!! Tablero actualizado !!\n")
                        impresionnueva(R, matriz)
                        # Evaluar si gano jugador
                        ganador,ganadasuser,ganadacompu,empate=ganaplayer(R, matriz,ganadasuser,ganadacompu,empate)
                        if ganador == True:
                            impresionderesultados(ganadasuser, ganadacompu, empate, name)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        matriz = computador(R, matriz)
                        print("!! Tablero actualizado !!\n")
                        impresionnueva(R, matriz)
                        # Evaluar si gano la maquina
                        ganador,ganadasuser,ganadacompu,empate=ganamaquina(R, matriz,ganadasuser,ganadacompu,empate)
                        if ganador == True:
                            impresionderesultados(ganadasuser, ganadacompu, empate, name)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break
                        # Resivar el empate
                        ganador, empate = buscarempate(R, matriz, empate)
                        if ganador == True:
                            impresionderesultados(ganadasuser, ganadacompu, empate, name)
                            Partida = str(input("Desea seguir jugando:(S) para si y (N) para no:"))
                            break





