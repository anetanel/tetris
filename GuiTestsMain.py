import time
from tkinter import *


def delete_last(event):
    for i in id:
        canvas.delete(i)
        print(f"deleted {i}")


def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def draw_shape(canvas, shape, xp=0, yp=0):
    size = 20
    id = []
    matrix = []
    if shape == 'l':
        matrix = [["X", ".", "."],
                  ["X", ".", "."],
                  ["X", "X", "."]]
        color = "orange"

    elif shape == 'o':
        matrix = [["X", "X"],
                  ["X", "X"]]
        color = "yellow"

    elif shape == 't':
        matrix = [["X", "X", "X"],
                  [".", "X", "."],
                  [".", ".", "."]]
        color = "magenta"

    elif shape == 'j':
        matrix = [[".", ".", "X"],
                  [".", ".", "X"],
                  [".", "X", "X"]]
        color = "blue"

    elif shape == 'i':
        matrix = [["X", ".", "."],
                  ["X", ".", "."],
                  ["X", ".", "."],
                  ["X", ".", "."]]
        color = "cyan"

    elif shape == 's':
        matrix = [[".", "X", "X"],
                  ["X", "X", "."],
                  [".", ".", "."],
                  [".", ".", "."]]
        color = "green"

    elif shape == 'z':
        matrix = [["X", "X", "."],
                  [".", "X", "X"],
                  [".", ".", "."],
                  [".", ".", "."]]
        color = "red"

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "X":
                id.append(canvas.create_rectangle(xp + x * size, yp + y * size, xp + x * size + size,
                                                  yp + y * size + size, fill=color))

    return id


root = Tk()
root.resizable(width=False, height=False)
frame_width = 640
frame_height = 480
root.geometry(f"{frame_width}x{frame_height}")
canvas = Canvas(root, height=frame_height, width=frame_width / 2, bg="grey")
canvas.create_rectangle(2, 2, frame_width / 2 + 1, frame_height - 3, width=3)
canvas.pack()

draw_shape(canvas, 'l', xp=10, yp=10)
draw_shape(canvas, 'i', xp=100, yp=10)
draw_shape(canvas, 't', xp=150, yp=10)
draw_shape(canvas, 'o', xp=250, yp=10)
draw_shape(canvas, 'j', xp=10, yp=100)
draw_shape(canvas, 's', xp=100, yp=100)
id = draw_shape(canvas, 'z', xp=200, yp=100)

while True:
    for i in (id):
        canvas.move(i, 0, 20)
    root.update()
    time.sleep(1)

root.bind("x", delete_last)
# root.bind("<Up>", rotate)
root.mainloop()
