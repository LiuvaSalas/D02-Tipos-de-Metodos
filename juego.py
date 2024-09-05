from personaje import Personaje
import random

print("¡Bienvenido a Gran Fantasía!\n")
nombre = input("Por favor indique el nombre de su personaje:\n")

mi_personaje = Personaje(nombre)
print(mi_personaje.estado)

print("\n¡Oh no!, ¡Ha aparecido un Orco!")
enemigo = Personaje("Orco")

print(mi_personaje.estado)
print(enemigo.estado)

probabilidad_ganar = mi_personaje.get_probabilidad_ganar(
    mi_personaje.nivel, enemigo.nivel
)

opcion_personaje = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)


while opcion_personaje == 1:
    aleatorio = random.uniform(0, 1)

    if aleatorio <= probabilidad_ganar:
        resultado = "G"
    else:
        resultado = "P"

    if resultado == "G":
        print(
            "\n¡Le has ganado al orco, felicidades!\n¡Recibiste 50 puntos de experiencia!\n"
        )
        mi_personaje.estado = 50
        enemigo.estado = -30

    else:
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!\n"
        )
        mi_personaje.estado = -30
        enemigo.estado = 50

    print(mi_personaje.estado)
    print(enemigo.estado)

    probabilidad_ganar = mi_personaje.get_probabilidad_ganar(
        mi_personaje.nivel, enemigo.nivel
    )
    opcion_personaje = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
print("\nHas huido, lo dejaste atras!\n")
