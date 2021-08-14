import random

nombres = ["Maria del Carmen","Luis","Leo","Maitte"]
preguntas = ["Introduccion y conclusiones","Mundo antiguo","Mundo Moderno","Institucionalizacio"]

for x in range(4):
    nombre = random.choice(nombres)
    pregunta = random.choice(preguntas)
    print(f"{nombre}: Pregunta {pregunta}")
    nombres.remove(nombre)
    preguntas.remove(pregunta)

