from tkinter import *


class Ball:
    def __init__(self, c: Canvas):
        self.UPDATE_RATE = 6  # update frame every UPDATE_RATE ms
        self.canvas = c
        self.c_height = self.canvas.winfo_height()
        self.c_width = self.canvas.winfo_width()
        size = 15
        # create ball in middle of field
        self.id = self.canvas.create_oval(self.c_width / 2, self.c_height / 2, self.c_width / 2 + size,
                                          self.c_height / 2 + size, fill="red")
        self.xv = 1  # x velocity
        self.yv = 1  # y velocity

    def draw(self):
        self.canvas.move(self.id, self.xv, self.yv)
        pos = self.canvas.coords(self.id)  # [x0, y0, x1, y1]
        # detect bounds collisions
        if pos[3] >= self.c_height:  # down
            self.yv = -self.yv
        if pos[1] <= 0:  # up
            self.yv = -self.yv
        if pos[2] >= self.c_width:  # right
            self.xv = -self.xv
        if pos[0] <= 0:
            self.xv = -self.xv  # left

        print(pos)
        self.canvas.after(self.UPDATE_RATE, self.draw)


root = Tk()
root.title("bounce!")
root.resizable(0, 0)
canvas = Canvas(root, width=640, height=480)
canvas.pack()
root.update()

ball = Ball(canvas)
ball.draw()

root.mainloop()
