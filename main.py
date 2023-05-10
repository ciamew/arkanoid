# import tkinter as tk
# import random
# win = tk.Tk()

# #width, height
# w = 750
# h = 600

# #cell_list = []

# canvas = tk.Canvas(width = w, height = h, bg = "white")
# canvas.pack()

# d=15
# movement = [1*d,1*d]

# colors = ["red", "orange", "yellow","green","blue","purple","pink","white","turquoise"]
# ball = canvas.create_oval(w/2-20,h/2-20,w/2,h/2, fill=random.choice(colors))

# bricks = []
# for i in range(0,5):
#     for s in range(1,6):
#         for u in range(0,10):
#             for n in range(1,11):
#                 bricks.append(canvas.create_rectangle(75*u ,30*i ,75*n ,30*s, outline="black",fill=random.choice(colors)))
# def move():
#     global movement
#     canvas.move(ball,movement[0],movement[1])
#     canvas.itemconfig(ball, fill=random.choice(colors))
#     if canvas.coords(ball)[0] < 0:
#         movement[0] *= (-1)
#     if canvas.coords(ball)[1] < 0:
#         movement[1] *= (-1)
#     if canvas.coords(ball)[2] > w:
#         movement[0] *= (-1)
#     if canvas.coords(ball)[3] > h:
#         movement[1] *= (-1)
#     canvas.after(50,move)

# move()

# win.mainloop()


import tkinter as tk
import random
win = tk.Tk()

#width, height
w = 650
h = 450

#cell_list = []

canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.pack()

d=15
movement = [1*d,1*d]

colors = ["red", "purple", "orange","yellow","blue","green","brown","magenta","turquoise"]
ball = canvas.create_oval(w/2-20,h/2-20,w/2,h/2, fill=random.choice(colors))
bricks_colors = ["black","darkblue","blue","turquoise"]

paddle = canvas.create_rectangle(w/2-50, h-80, w/2+50, h-60, fill="black")

bricks_w = 65
bricks_h = 20

brick_count_x = 10
brick_count_y = 4

bricks = []

def makebricks():
    for y in range(brick_count_y):
        for x in range(brick_count_x):
            bricks.append(canvas.create_rectangle(x*bricks_w, y*bricks_h, x*bricks_w + bricks_w, y*bricks_h + bricks_h, fill = bricks_colors[y%brick_count_y],width=5,outline="white"))
makebricks()

# bricks = []
# for i in range(0,4):
#     for s in range(1,5):
#         for u in range(0,10):
#             for n in range(1,11):
#                 bricks.append(canvas.create_rectangle(75*u ,30*i ,75*n ,30*s, outline="black",fill=random.choice(colors)))


def destroybrick():
    global movement
    coords_ball = canvas.coords(ball)
    # print(coords_ball)
    items_list = canvas.find_overlapping(coords_ball[0],coords_ball[1],coords_ball[2],coords_ball[3])
    print(items_list)
    for i in items_list:
        if i in bricks:
            bricks.remove(i)
            canvas.delete(i)
            movement = [movement[0] * -1, movement[1] * -1]





def ball_move():
    global movement
    canvas.move(ball,movement[0],movement[1])
    canvas.itemconfig(ball, fill=random.choice(colors))
    destroybrick()
    if canvas.coords(ball)[0] < 0:
        movement[0] *= (-1)
    if canvas.coords(ball)[1] < 0:
        movement[1] *= (-1)
    if canvas.coords(ball)[2] > w:
        movement[0] *= (-1)
    if canvas.coords(ball)[3] > h:
        movement[1] *= (-1)
    canvas.after(50,ball_move)

def starter(e):
    global x
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if paddle in zoz:
        x = e.x
        ball_move()

def mover(e):
    global x
    if x != 0:
        mouse = e.x - x
        canvas.move(paddle, mouse, 0)
        x = e.x

# def moverarrow(j):
#     global x
#     if x != 0:
#         arrow = e.x - x
#         canvas.move(paddle, arrow, 0)
#         x = e.x


def checkkey(s):
    print("Stlacila som")
    print(s.char)

canvas.bind("<Button-1>", starter)
canvas.bind("<B1-Motion>", mover)
win.bind("<Key>",checkkey)
win.bind("<Up>",checkkey)
win.bind("<Down>",checkkey)
win.bind("<Right>",checkkey)
win.bind("<Left>",checkkey)


win.mainloop()
