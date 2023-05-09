import tkinter as tk
import random
win = tk.Tk()

#width, height
w = 750
h = 600

#cell_list = []

canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.pack()

d=15
movement = [1*d,1*d]

colors = ["red", "orange", "yellow","green","blue","purple","pink","white","turquoise"]
ball = canvas.create_oval(w/2-20,h/2-20,w/2,h/2, fill=random.choice(colors))


def move():
    global movement
    canvas.move(ball,movement[0],movement[1])
    canvas.itemconfig(ball, fill=random.choice(colors))
    if canvas.coords(ball)[0] < 0:
        movement[0] *= (-1)
    if canvas.coords(ball)[1] < 0:
        movement[1] *= (-1)
    if canvas.coords(ball)[2] > w:
        movement[0] *= (-1)
    if canvas.coords(ball)[3] > h:
        movement[1] *= (-1)
    canvas.after(50,move)

move()

win.mainloop()