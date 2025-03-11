import turtle


pantalla = turtle.Screen()
pantalla.bgcolor("black")
pantalla.title("Trayectoria de regreso desde Marte")


nave = turtle.Turtle()
nave.color("white")
nave.speed(3)

trayectoria_regreso = [
    (180, 40), 
    (270, 20), 
    (180, 58),  
    (270, 48),  
    (0, 25),   
    (270, 27),   
    (180, 58),   
    (90, 12),  
    (180, 25)  
]


nave.penup()
nave.goto(200, 100)
nave.pendown()


for angulo, distancia in trayectoria_regreso:
    nave.setheading(angulo)  
    nave.forward(distancia)  


pantalla.mainloop()