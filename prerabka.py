
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
# bar = canvas.create_rectangle(0,h,w,h,outline="red")
# barr = canvas.create_polygon(0,h, 5,440, 10,h, 15,440, 20,h, 25,440, 30,h, 35,440,40,h,45,440,50,h,55,440,60,h,65,440,70,h,75,440,80,h,85,440,90,h,95,440,100,h,105,440,110,h,115,440,120,h,0,h)

# for q in range(65):
#     for bw in range(0, 130, 5):
#         for bh in range(h, 440):
#             canvas.create_polygon(bw,bh,bw)
#
# for bw in range(0,130,5):
#     for bh in range (h,440):
#         canvas.create_rectangle()


for q in range(0,64):
    for e in range(1,65):
        for bw1 in range(10):
            for bw2 in range(5): #5+10*e
                canvas.create_polygon(bw1*q,h,bw2+10*e,440)


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
#    canvas.after(25,destroybrick)


def ball_move():
    global movement
    canvas.move(ball,movement[0],movement[1])
    canvas.itemconfig(ball, fill=random.choice(colors))
    paddle_pos = canvas.coords(paddle)
    overlap = canvas.find_overlapping(paddle_pos[0], paddle_pos[1], paddle_pos[2], paddle_pos[3])
    destroybrick()
    if canvas.coords(ball)[0] < 0:
        movement[0] *= (-1)
    if canvas.coords(ball)[1] < 0:
        movement[1] *= (-1)
    if canvas.coords(ball)[2] > w:
        movement[0] *= (-1)
    if canvas.coords(ball)[3] > h:
        canvas.delete("all")
        canvas.create_text(w/2, h/2, text="YOU LOST", fill="red", font="Arial 15")
    if ball in overlap:
        movement = bounce(canvas.coords(ball), paddle_pos)
    canvas.after(50, ball_move)

paddle_width = 50
def bounce(ball_pos, paddle_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    paddle_middle = (paddle_pos[0] + paddle_pos[2])//2
    ball_to_rec = ball_pos - paddle_middle
    return [ball_to_rec//(paddle_width//3), -1]

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
