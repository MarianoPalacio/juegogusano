import turtle
import time
import random
import os

# Vidas
Vidas = 3

# Posponer
posponer = 0.1

# Mensaje
mensaje = "mensaje"

# Mensaje Bonus
bmensaje = "bmensaje"

# Demora
demora = "demora"
demora = 1

# Puntaje
score = 0
high_score = 0

# Bonus Puntaje y Comida
bonus = "bonus"
bonus = 175
bonus2 = 200
comida_bonus = "cb"

# Configuracion Pantalla
wn = turtle.Screen()
wn.title("Gusano Diabólico")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# Cabeza de Gusano
cabeza = turtle.Turtle()
cabeza.speed(0)  # Deja la cabeza del Gusano quieto
cabeza.shape("square")
cabeza.color("red")
cabeza.penup()  # Esto es para que al desplasarce no deje rastro.
# Posicionamos la cabeza en la pantalla, segùn ejes cartecianos.
cabeza.goto(0, 0)
cabeza.direction = "stop"

# Morfi del Gusano
morfi = turtle.Turtle()
morfi.speed(0)
morfi.shape("circle")
morfi.color("white")
morfi.penup()  # Esto es para que al desplasarce no deje rastro.
morfi.goto(0, 100)  # Posicionamos del morfi random en la pantalla.

# Cuerpo Gusano
segmentos = []

# Texto en pantalla
texto = turtle.Turtle()
texto.speed(0)
texto.color("orange")
texto.penup()
texto.hideturtle()
texto.goto(0, 260)
texto.write("Vidas: 3   Puntaje: 0	  Puntaje Alto: 0",
            align="center", font=("Courier", 20, "normal"))

# Funciones


def arriba():
    cabeza.direction = "up"


def abajo():
    cabeza.direction = "down"


def izquierda():
    cabeza.direction = "left"


def derecha():
    cabeza.direction = "right"


def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)


# Teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")

while True:
    wn.update()

    # Choques Pared
    if cabeza.xcor() > 285 or cabeza.xcor() < -285 or cabeza.ycor(
    	) > 285 or cabeza.ycor() < -285:
        os.system("afplay Gong.mp3&")
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Esconder cuerpo
        for segmento in segmentos:
            segmento.goto(1000, 1000)

        # Mostrar Texto
        mensaje = turtle.Turtle()
        mensaje.color("red")
        mensaje.penup()
        mensaje.hideturtle()
        mensaje.goto(0, 0)
        mensaje.write("Chocaste", align="center",
                      font=("Courier", 50, "normal"))
        mensaje.speed(0)
        Vidas -= 1

        # Reiniciar Puntaje
        score = 0
        texto.clear()
        texto.write("Vidas: {}  Puntaje: {}  Puntaje Alto: {}".format(
            Vidas, score, high_score), align="center", font=("Courier", 20, "normal"))

        # Reiniciar Velocidad
        posponer = 0.1

        # esconder
        segmentos.clear()

        # Borrar mensaje
        mensaje.clear()
        time.sleep(demora)

    # Comer Morfi
    if cabeza.distance(morfi) < 20:
        os.system("afplay Beep.mp3&")
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        morfi.goto(x, y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("green")
        # Esto es para que al desplasarce no deje rastro.
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        # Incrementar Velocidad
        posponer -= 0.001

        # Sumar puntaje
        score += 10
        # Multiplicador Bonus
        if score == 100:
            os.system("afplay Horn.mp3&")
            score += bonus
            bmensaje = turtle.Turtle()
            bmensaje.color("red")
            bmensaje.penup()
            bmensaje.hideturtle()
            bmensaje.goto(0, 0)
            bmensaje.write("GANASTE BONUS", align="center",
                           font=("Courier", 90, "normal"))
            bmensaje.speed(0)
            # Borrar mensaje REVISAR QUE EL MENSAJE DESAPARECE RÀPIDO
            bmensaje.clear()
            time.sleep(0)

        if score == 475:
            os.system("afplay Horn.mp3&")
            score += bonus2

        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Vidas: {}  Puntaje: {}  Puntaje Alto: {}".format(
            Vidas, score, high_score), align="center", font=("Courier", 20, "normal"))

    totalSeg = len(segmentos)
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index - 1].ycor()
        segmentos[index].goto(x, y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x, y)

    mov()
    # Choque con nuestro cuerpo de gusano
    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            os.system("afplay Gong.mp3&")
            time.sleep(1)
            cabeza.goto(0, 0)
            cabeza.direction = "stop"

            # Esconder restos
            for segmento in segmentos:
                segmento.goto(1000, 1000)
            segmentos.clear()

            # Mostrar Texto Choque con Cuerpo Gusano
            mensaje = turtle.Turtle()
            mensaje.color("red")
            mensaje.penup()
            mensaje.hideturtle()
            mensaje.goto(0, 0)
            mensaje.write("OUCH PERDISTE", align="center",
                          font=("Courier", 50, "normal"))
            mensaje.speed(0)
            Vidas -= 1

            # Reiniciar Puntaje
            score = 0
            texto.clear()
            texto.write("Vidas: {}  Puntaje: {}  Puntaje Alto: {}".format(
                Vidas, score, high_score), align="center", font=("Courier", 20, "normal"))

            # Reiniciar Velocidad
            posponer = 0.1

            # Borrar mensaje
            mensaje.clear()
            time.sleep(demora)

    time.sleep(posponer)

Gusano2.main_loop()
