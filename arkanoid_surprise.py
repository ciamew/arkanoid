import tkinter as tk
import random

win = tk.Tk()

#width, height
w = 650
h = 450

#cell_list = []

canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.pack()

text_start = canvas.create_text(w//2, h//2 - 70, text="START THE GAME BY CLICKING \n              ON THE PADDLE")

d=15
movement = [-1*d,-1*d]

colors = ["red", "purple", "orange","yellow","blue","green","brown","magenta","turquoise"]
ball = canvas.create_oval(w/2-10,h/2-10,w/2+10,h/2+10, fill=random.choice(colors))
bricks_colors = ["black","darkblue","blue","turquoise"]

paddle = canvas.create_rectangle(w/2-50, h-80, w/2+50, h-60, fill="black")

bar = canvas.create_rectangle(0,h,w,h,outline="red")
for q in range(0,66):  #vytvori spodne trojuholniky
    canvas.create_polygon(10*q,450,5+(10*q),440,10*(q+1),450,outline="red",fill="red")

ball_speed_text = canvas.create_text(67,350,text="BALL SPEED")
#speed_up_rect = canvas.create_rectangle(40,370,64,394,outline="white")
speed_up_plus = canvas.create_polygon(48,370,56,370,56,378,64,378,64,386,56,386,56,386,56,394,48,394,48,386,40,386,40,378,48,378,fill="darkblue",outline="darkblue")
#speed_down_rect = canvas.create_rectangle(70,370,94,394,outline="white")
speed_down_minus = canvas.create_rectangle(70,378,94,386,fill="darkblue",outline="darkblue")


change_bg_color_text = canvas.create_text(520,255,text="CHANGE BACKGROUND COLOR --->\n(by clicking on the given number)")
bg_white = canvas.create_rectangle(620,240,640,260,fill="white")
bg_white_text = canvas.create_text(630,250,text="1")
bg_beige = canvas.create_rectangle(620,270,640,290,fill="beige")
bg_beige_text = canvas.create_text(630,280,text="2")
bg_yellow = canvas.create_rectangle(620,300,640,320,fill="yellow")
bg_yellow_text = canvas.create_text(630,310,text="3")
bg_orange = canvas.create_rectangle(620,330,640,350,fill="orange")
bg_orange_text = canvas.create_text(630,340,text="4")
bg_darkkhaki = canvas.create_rectangle(620,360,640,380,fill="darkkhaki")
bg_darkkhaki_text = canvas.create_text(630,370,text="5")

def change_bg(e):
    # print("you pressed"+ e.char)
    if e.char == "1":
        # print("ide")
        canvas.configure(bg="white")
    if e.char == "2":
        canvas.configure(bg="beige")
    if e.char == "3":
        canvas.configure(bg="yellow")
    if e.char == "4":
        canvas.configure(bg="orange")
    if e.char == "5":
        canvas.configure(bg="darkkhaki")

for bg in range(1,6):
    win.bind(str(bg), change_bg)

bricks_w = 65
bricks_h = 20

brick_count_x = 10
brick_count_y = 4

bricks = []

def makebricks():
    for y in range(brick_count_y):
        for x in range(brick_count_x):
            bricks_feature = canvas.create_rectangle(x * bricks_w, y * bricks_h, x * bricks_w + bricks_w,y * bricks_h + bricks_h, fill=bricks_colors[y % brick_count_y],width=5, outline="white")
            # bricks.append(canvas.create_rectangle(x*bricks_w, y*bricks_h, x*bricks_w + bricks_w, y*bricks_h + bricks_h, fill = bricks_colors[y%brick_count_y],width=5,outline="white"))
            bricks.append(bricks_feature)
makebricks()



def destroybrick():
    global movement
    coords_ball = canvas.coords(ball)
    # print(coords_ball)
    items_list = canvas.find_overlapping(coords_ball[0],coords_ball[1],coords_ball[2],coords_ball[3])
    print(items_list)
    for i in items_list:
        if i in bricks:
            movement = [movement[0] * -1, movement[1] * -1]
            bricks.remove(i)
            canvas.delete(i)
            # movement = [movement[0] * -1, movement[1] * -1]
#    canvas.after(25,destroybrick)


def ball_move():
    global movement
    canvas.move(ball,movement[0],movement[1])
    canvas.itemconfig(ball, fill=random.choice(colors))
    paddle_pos = canvas.coords(paddle)
    overlap = canvas.find_overlapping(paddle_pos[0], paddle_pos[1], paddle_pos[2], paddle_pos[3])
    destroybrick()
    canvas.after(50, ball_move)
    if canvas.coords(ball)[0] < 0:
        movement[0] *= (-1)
    if canvas.coords(ball)[1] < 0:
        movement[1] *= (-1)
    if canvas.coords(ball)[2] > w:
        movement[0] *= (-1)
    if canvas.coords(ball)[3] > (h-10):
        canvas.delete("all")
        canvas.create_text(w/2, h/2, text="                                    YOU LOST \n TRY AGAIN BY RESTARTING THE WHOLE GAME", fill="red", font="Arial 9")
        starter()
    if ball in overlap:
        movement = bounce(canvas.coords(ball), paddle_pos)
    # canvas.after(100, ball_move)

paddle_width = 50
def bounce(ball_pos, paddle_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    paddle_middle = (paddle_pos[0] + paddle_pos[2])//2
    ball_to_rec = ball_pos - paddle_middle
    return [ball_to_rec//(paddle_width//3), -1]

def starter(e):
    global x, y
    click = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if paddle in click:
        x = e.x
        y = e.y
        ball_move()
        canvas.delete(text_start,speed_up_plus,ball_speed_text,speed_down_minus,change_bg_color_text,speed)
        #canvas.delete("all")

def mover(e):
    global x
    if x != 0:
        mouse = e.x - x
        canvas.move(paddle, mouse, 0)
        x = e.x

speed = canvas.create_text(w//2,420,text="(to make the ball faster,you have to click on the paddle several times) \n                                               idk y",font="Arial 7")
# def speed():
#     canvas.after(50,ball_move)

# def checkkey(s):
#     print("Stlacila som")
#     print(s.char)

canvas.bind("<Button-1>", starter)
canvas.bind("<B1-Motion>", mover)
# canvas.bind("<Button-1>", speedup)
# win.bind("<Key>",checkkey)
# win.bind("<Up>",speed)
# win.bind("<Down>",checkkey)
# win.bind("<Right>",checkkey)
# win.bind("<Left>",checkkey)

win.mainloop()
