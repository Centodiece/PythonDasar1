import turtle

# Membuat objek turtle
pen = turtle.Turtle()

# Mengatur kecepatan menggambar
pen.speed(1)

# Menggambar persegi panjang dengan warna merah
pen.fillcolor("red")
pen.begin_fill()
for _ in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# Jarak antara persegi panjang dan segitiga
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Menggambar segitiga dengan warna kuning
pen.fillcolor("yellow")
pen.begin_fill()
for _ in range(3):
    pen.forward(100)
    pen.left(120)
pen.end_fill()

# Jarak antara segitiga dan trapesium
pen.penup()
pen.goto(300, 0)
pen.pendown()

# Menggambar trapesium dengan warna hijau
pen.fillcolor("green")
pen.begin_fill()
for _ in range(4):
    pen.forward(80)
    pen.left(90)
pen.end_fill()

# Jarak antara trapesium dan jajar genjang
pen.penup()
pen.goto(430, 0)
pen.pendown()

# Menggambar jajar genjang dengan warna biru
pen.fillcolor("blue")
pen.begin_fill()
pen.goto(480, 0)
pen.goto(430, 50)
pen.goto(350, 50)
pen.goto(400, 0)
pen.end_fill()

# Jarak antara jajar genjang dan segilima
pen.penup()
pen.goto(550, 0)
pen.pendown()

# Menggambar segilima dengan warna ungu
pen.fillcolor("purple")
pen.begin_fill()
for _ in range(5):
    pen.forward(60)
    pen.left(72)
pen.end_fill()

# Menutup jendela turtle
turtle.done()