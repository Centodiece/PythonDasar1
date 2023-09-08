import turtle

# Membuat jendela grafis
wn = turtle.Screen()
wn.bgcolor("white")

# Membuat objek turtle
mobil = turtle.Turtle()
mobil.color("blue")

# Menggambar badan mobil
mobil.begin_fill()
mobil.forward(200)
mobil.left(90)
mobil.forward(50)
mobil.left(90)
mobil.forward(200)
mobil.left(90)
mobil.forward(50)
mobil.end_fill()

# Menggambar roda mobil
mobil.penup()
mobil.goto(50, -10)
mobil.pendown()
mobil.color("black")
mobil.begin_fill()
mobil.circle(25)
mobil.end_fill()

mobil.penup()
mobil.goto(150, -10)
mobil.pendown()
mobil.begin_fill()
mobil.circle(25)
mobil.end_fill()

# Tutup jendela grafis saat mengklik
wn.exitonclick()