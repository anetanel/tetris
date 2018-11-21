import time
from tkinter import *
import random


class Paddle:
    def __init__(self, c: Canvas, color):
        self.canvas = c
        pd_w = 100
        pd_h = 20
        self.velocity = 15
        self.id = c.create_rectangle(c.winfo_width() / 2 - pd_w / 2, c.winfo_height() - 2 * pd_h,
                                     c.winfo_width() / 2 + pd_w / 2, c.winfo_height() - pd_h,
                                     fill=color)
        c.bind_all("<Left>", self.move_left)
        c.bind_all("<Right>", self.move_right)

    def move_left(self, event):
        self._move(-self.velocity)

    def move_right(self, event):
        self._move(self.velocity)

    def _move(self, velocity):
        pos = self.canvas.coords(self.id)  # [x0, y0, x1, y1]
        if pos[0] + velocity <= 0 and velocity < 0:  # left
            velocity = -pos[0]  # snap to left
        elif pos[2] + velocity >= self.canvas.winfo_width() and velocity > 0:  # right
            velocity = self.canvas.winfo_width() - pos[2] - 1  # snap to right

        self.canvas.move(self.id, velocity, 0)
        # print(self.canvas.coords(self.id))

    def position(self):
        return _pos_dict(self.canvas.coords(self.id))


class Ball:

    def __init__(self, c: Canvas, p: Paddle, color):
        self.canvas = c
        self.paddle = p
        self.alive = True
        self.grace = 0
        self.UPDATE_RATE = 5  # update frame every UPDATE_RATE ms
        self.c_height = c.winfo_height()
        self.c_width = c.winfo_width()
        size = 15
        # create ball in middle of field
        self.id = c.create_oval(self.c_width / 2, self.c_height / 2, self.c_width / 2 + size,
                                self.c_height / 2 + size, fill=color)
        xv_list = [-1.4, -1.3, -1.2, -1.1, -1, 1, 1.2, 1.3,
                   1.4]  # list of initial xv. to make every game a bit different
        self.xv = random.sample(xv_list, 1)[0]  # x velocity
        self.yv = -1  # y velocity

    def draw(self):
        self.canvas.move(self.id, self.xv, self.yv)
        pos = _pos_dict(self.canvas.coords(self.id))  # [x0, y0, x1, y1]
        # detect bounds collisions
        if pos["y1"] >= self.c_height:  # down
            # self.yv = -self.yv
            game_over(self)
        if pos["y0"] <= 0:  # up
            self.yv = -self.yv
        if pos["x1"] >= self.c_width:  # right
            self.xv = -self.xv
        if pos["x0"] <= 0:
            self.xv = -self.xv  # left

        # detect paddle collision
        # print(self.grace)
        if self.grace > 0:
            self.grace -= 1
        p_pos = self.paddle.position()
        if pos["y1"] >= p_pos["y0"] and p_pos["x0"] <= pos["x1"] <= p_pos["x1"]:
            if self.grace <= 0:
                self.yv = -self.yv
                self.grace = 30

        # print(pos)
        if self.alive:
            self.canvas.after(self.UPDATE_RATE, self.draw)


def _pos_dict(pos_list: list):
    d = {"x0": pos_list[0],
         "y0": pos_list[1],
         "x1": pos_list[2],
         "y1": pos_list[3]}
    return d


def new_ball():
    ball = Ball(canvas, paddle, "red")
    ball.draw()


def game_over(ball: Ball):
    ball.alive = False
    canvas.delete(ball.id)
    print("Game Over!")
    time.sleep(1)
    new_ball()


root = Tk()
root.title("bounce!")
root.resizable(0, 0)
canvas = Canvas(root, width=640, height=480, bd=0, highlightthickness=0)
canvas.pack()
root.update()

paddle = Paddle(canvas, "green")
new_ball()

root.mainloop()
