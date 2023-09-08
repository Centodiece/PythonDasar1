import turtle

# Fungsi untuk menggambar pohon Fibonacci
def fibonacci_tree(t, branch_len, angle, depth):
    if depth > 0:
        t.forward(branch_len)
        t.right(angle)
        fibonacci_tree(t, branch_len - 10, angle, depth - 1)
        t.left(2 * angle)
        fibonacci_tree(t, branch_len - 10, angle, depth - 1)
        t.right(angle)
        t.backward(branch_len)

# Setup turtle
wn = turtle.Screen()
wn.bgcolor("white")
t = turtle.Turtle()
t.color("green")
t.width(2)
t.left(90)
t.up()
t.backward(100)
t.down()

# Gambar pohon Fibonacci
fibonacci_tree(t, 80, 30, 7)

# Tutup jendela saat selesai
wn.exitonclick()