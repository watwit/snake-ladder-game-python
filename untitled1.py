from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
sky_id = canvas.create_rectangle(0, 0, 400, 300, fill='blue')
floor_id = canvas.create_rectangle(0, 300, 400, 400, fill='brown')
sheep_image = PhotoImage(file='whitesheepright.gif')
sheep_id = canvas.create_image(0, 300, anchor=SW, image=sheep_image)
for i in range(80):
    canvas.move(sheep_id, 5, 0)

    tk.update()
    time.sleep(0.05)