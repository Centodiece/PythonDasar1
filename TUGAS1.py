import turtle

# Membuat objek Turtle
t = turtle.Turtle()

# Menggambar persegi panjang
for _ in range(2):
    t.forward(200)  # Panjang sisi
    t.left(90)      # Sudut siku-siku
    t.forward(100)  # Lebar sisi
    t.left(90)
    
# Jarak antara persegi panjang dan segitiga
t.penup()
t.forward(300)
t.pendown()

# Menggambar segitiga
for _ in range(3):
    t.forward(200)  # Panjang sisi
    t.left(120)     # Sudut segitiga

# Jarak antara segitiga dan trapesium
t.penup()
t.goto(0, 0)
t.pendown()

# Menggambar trapesium
for _ in range(4):
    if _ % 2 == 0:
        t.forward(150)  # Panjang sisi atas
        t.left(60)      # Sudut trapesium
    else:
        t.forward(100)  # Panjang sisi bawah
        t.left(120)     # Sudut trapesium
        
# Jarak antara trapesium dan jajar genjang
t.penup()
t.goto(350, 0)
t.pendown()

# Menggambar jajar genjang
for _ in range(2):
    t.forward(200)  # Panjang sisi atas/bawah
    t.left(60)      # Sudut jajar genjang
    t.forward(100)  # Panjang sisi samping
    t.left(120)     # Sudut jajar genjang

# Jarak antara jajar genjang dan belah ketupat
t.penup()
t.goto(0, -200)
t.pendown()

# Menggambar belah ketupat
for _ in range(2):
    t.forward(100)  # Panjang diagonal 1
    t.left(45)      # Sudut belah ketupat
    t.forward(100)  # Panjang diagonal 2
    t.left(135)     # Sudut belah ketupat

# Menutup jendela ketika selesai
turtle.done()