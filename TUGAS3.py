import turtle

# Membuat objek turtle
bendera = turtle.Turtle()
bendera.speed(0)  # Kecepatan menggambar

# Menggambar latar belakang putih
bendera.penup()
bendera.goto(-300, 200)
bendera.pendown()
bendera.color("white")
bendera.begin_fill()
bendera.forward(600)
bendera.right(90)
bendera.forward(400)
bendera.right(90)
bendera.forward(600)
bendera.right(90)
bendera.forward(400)
bendera.end_fill()

# Menggambar warna merah atas bendera
bendera.penup()
bendera.goto(-300, 200)
bendera.pendown()
bendera.color("red")
bendera.begin_fill()
bendera.forward(600)
bendera.right(90)
bendera.forward(200)
bendera.right(90)
bendera.forward(600)
bendera.right(90)
bendera.forward(200)
bendera.end_fill()

# Menutup jendela turtle
turtle.done()