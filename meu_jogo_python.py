import turtle
import time
import random

# Configuração da tela
janela = turtle.Screen()
janela.title("Jogo da Cobrinha")
janela.bgcolor("black")
janela.setup(width=600, height=600)
janela.tracer(0)

# Cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("green")
cabeca.penup()
cabeca.goto(0,0)
cabeca.direction = "stop"

# Comida (Maçã)
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

corpo = []

# Funções de movimento
def subir():
    if cabeca.direction != "down":
        cabeca.direction = "up"

def descer():
    if cabeca.direction != "up":
        cabeca.direction = "down"

def esquerda():
    if cabeca.direction != "right":
        cabeca.direction = "left"

def direita():
    if cabeca.direction != "left":
        cabeca.direction = "right"

def mover():
    if cabeca.direction == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)
    if cabeca.direction == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)
    if cabeca.direction == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)
    if cabeca.direction == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

# Teclado
janela.listen()
janela.onkeypress(subir, "w")
janela.onkeypress(descer, "s")
janela.onkeypress(esquerda, "a")
janela.onkeypress(direita, "d")

# Loop principal
rodando = True
while rodando:
    try:
        janela.update()

        # Verifica colisão com a borda
        if cabeca.xcor() > 290 or cabeca.xcor() < -290 or cabeca.ycor() > 290 or cabeca.ycor() < -290:
            time.sleep(1)
            cabeca.goto(0,0)
            cabeca.direction = "stop"
            for segmento in corpo:
                segmento.goto(1000, 1000)
            corpo.clear()

        # Verifica colisão com a comida
        if cabeca.distance(comida) < 20:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            comida.goto(x, y)

            novo_segmento = turtle.Turtle()
            novo_segmento.speed(0)
            novo_segmento.shape("square")
            novo_segmento.color("grey")
            novo_segmento.penup()
            corpo.append(novo_segmento)

        # Move o corpo
        for index in range(len(corpo)-1, 0, -1):
            x = corpo[index-1].xcor()
            y = corpo[index-1].ycor()
            corpo[index].goto(x, y)

        if len(corpo) > 0:
            x = cabeca.xcor()
            y = cabeca.ycor()
            corpo[0].goto(x, y)

        mover()
        time.sleep(0.1)
        
    except:
        # Se a janela for fechada, encerra o loop sem erro
        rodando = False