import turtle

def dibujar_cuadro():
        turtle.pensize(5)
        turtle.color("red")
        turtle.penup()
        turtle.goto(-150,150)
        turtle.pendown()
        
        for _ in range(4):
           turtle.forward(300)
           turtle.right(90)
        
def dibujar_rectangulo(x, y, width, height):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("red")
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()
    
def dibujar_cruz_roja():
    dibujar_rectangulo(-50, 150, 100, 300) 
    dibujar_rectangulo(-150,50,300,100) 
        
turtle.speed(1)

dibujar_cuadro()
dibujar_cruz_roja()
dibujar_rectangulo()

turtle.hideturtle()
turtle.done()




    
