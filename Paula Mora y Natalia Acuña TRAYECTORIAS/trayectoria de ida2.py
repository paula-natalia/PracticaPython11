import turtle


pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Trayectoria a Marte")


nave = turtle.Turtle()
nave.color("white")
nave.speed(3)


trayectoria = [
    (90, 25),  
    (0, 35),   
    (90, 45),  
    (0, 52),   
    (270, 85),  
    (0, 55),
    (90, 47),
    (0, 30),   
    (90, 35)   
]


nave.penup()
nave.goto(-200, -100)  
nave.pendown()


for angulo, distancia in trayectoria:
    nave.setheading(angulo)  
    nave.forward(distancia)  


pantalla.mainloop()