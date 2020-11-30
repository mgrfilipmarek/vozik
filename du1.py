import tkinter

canvas = tkinter.Canvas(width=600, height=200)
canvas.pack()

obr = tkinter.PhotoImage(file='vozik.png')
canvas.create_image(500, 100, image=obr)
canvas.create_image(200, 100, image=obr)
