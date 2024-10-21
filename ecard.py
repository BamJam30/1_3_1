# Import module 
import turtle 
import tkinter
import time
from tkinter import PhotoImage

# create background
pg = turtle.Screen()
pg.title("BrawlStars-Hoco")
pg.bgpic("IMG_1329-ezgif.com-resize (4).GIF")
pg.setup(1300,940)

#Card base
root = tkinter.Tk()
root.title("E-Card")
image = PhotoImage(file="nitatextbubble.jpg")  # Ensure this file is a supported format
label = tkinter.Label(root, image=image)
label.pack()

# create ecard base
root = tkinter.Tk()
root.title("E-Card")
image = PhotoImage(file="nitatextbubble.jpg")
label = tkinter.Label(pg, image=image)
label.pack()


# Write text on card
def write_text(text, x, y, font_size=20, color="black"):
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(x, y)
    writer.color(color)
    writer.hideturtle()
    writer.write(text, align="center", font=("Arial", font_size, "bold"))
    return writer

# Animates text
def animate_text(text, x, y, font_size=20):
    writer = turtle.Turtle()
    writer.penup()
    writer.goto(x, y)
    writer.hideturtle()
   
    # Fade-in effect
    for alpha in range(0, 256, 5):
        writer.color((1, 0, 0, alpha / 255))  # Use RGBA for fade
        writer.write(text, align="center", font=("Arial", font_size, "bold"))
        pg.update()
        time.sleep(0.02)
        writer.clear()  # Clear previous text

    writer.write(text, align="center", font=("Arial", font_size, "bold"))
def run_tkinter():
    root.update()
    root.after(100, run_tkinter)


run_tkinter()
# Start the Tkinter loop
pg.mainloop()
