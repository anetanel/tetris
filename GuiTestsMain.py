from tkinter import *


def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix


def draw_shape(canvas, shape, xp=0, yp=0):
    matrix = []
    if shape == 'i':
        matrix = [["X", ".", "."],
                  ["X", ".", "."],
                  ["X", ".", "."],
                  ["X", ".", "."]]
        color = "green"
    elif shape == 't':
        matrix = [["X", "X", "X"],
                  [".", "X", "."],
                  [".", ".", "."]]
        color = "blue"
    elif shape == 'l':
        matrix = [["X", ".", "."],
                  ["X", ".", "."],
                  ["X", "X", "."]]
        color = "red"
    size = 20

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "X":
                canvas.create_rectangle(xp + x * size, yp + y * size, xp + x * size + size,
                                        yp + y * size + size, fill=color)


root = Tk()
root.resizable(width=False, height=False)
frame_width = 640
frame_height = 480
root.geometry(f"{frame_width}x{frame_height}")
canvas = Canvas(root, height=frame_height, width=frame_width / 2, bg="grey")
canvas.create_rectangle(2, 2, frame_width / 2 + 1, frame_height - 3, width=3)
canvas.pack()

draw_shape(canvas, 'l', xp=10)
draw_shape(canvas, 'i', xp=100)
draw_shape(canvas, 't', xp=200)


# root.bind("<Up>", rotate)
root.mainloop()
