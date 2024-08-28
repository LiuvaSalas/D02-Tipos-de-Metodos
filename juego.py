from personaje import Personaje
import random

print("¡Bienvenido a Gran Realidad!\n")
nombre = input(
    "Por favor indique el nombre de su personaje:\n"
)

p = Personaje(nombre)
print(p.estado)

print(
    "\n¡Oh no!, ¡Ha aparecido un Orco!"
)
o = Personaje("Orco")

print(p.estado)
print(o.estado)

probabilidad_ganar = p.get_probabilidad_ganar(p.experiencia, o.experiencia)

opcion_personaje = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

if opcion_personaje == 1:
    while opcion_personaje == 1:
        aleatorio = random.uniform(0, 1)

        if aleatorio <= probabilidad_ganar:
            resultado = "G"
        else:
            resultado = "P"

        if resultado == "G":
            print(
                "\n¡Le has ganado al orco, felicidades!\n¡Recibirás 50 puntos de experiencia!\n"
            )
            p.estado = 50
            o.estado = -30

        else:
            print(
                "\n¡Oh no! ¡El orco te ha ganado!\n¡Has perdido 30 puntos de experiencia!\n"
            )
            p.estado = -30
            o.estado = 50

        print(p.estado)
        print(o.estado)

        probabilidad_ganar = p.get_probabilidad_ganar(p.experiencia, o.experiencia)
        opcion_personaje = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
    print("\nDont worry, ¡Lo dejaste atras!\n")