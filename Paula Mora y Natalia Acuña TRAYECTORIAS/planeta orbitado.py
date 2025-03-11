import turtle
turtle.speed(1)
    
def dibujar_cuadro():
        for _ in range(4):
            turtle.forward(150)
            turtle.right(90)
            
dibujar_cuadro()


turtle.penup()
turtle.goto(150,0)
turtle.pendown()
dibujar_cuadro()

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()
dibujar_cuadro()

turtle.penup()
turtle.goto(150,-150)
turtle.pendown()
dibujar_cuadro()

turtle.done()
