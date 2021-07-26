import random

nombres = ["Carmen","Lucia","Vanessa","Luis"]
preguntas = [1,2,3,4]

for x in range(4):
    nombre = random.choice(nombres)
    pregunta = random.choice(preguntas)
    print(f"{nombre}: Pregunta {pregunta}")
    nombres.remove(nombre)
    preguntas.remove(pregunta)

