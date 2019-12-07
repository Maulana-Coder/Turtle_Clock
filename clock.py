import turtle
import time

# Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height= 600)
wn.title("Clock - Maulana ID")
wn.tracer(0)

# Create Pen For Draw
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def about():
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-50, -280)
    turtle.write("Created By\nMaulana ID", font=("Consolas", 15, "bold",))
    turtle.penup()
    turtle.hideturtle()
about()

def draw_clock(h, m, s, pen):

    # Draw Clock Face
    pen.penup()
    pen.goto(0, 210)
    pen.setheading(180)
    pen.color("lime")
    pen.pendown()
    pen.circle(210)

    # Draw Line Hours
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)

    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0, 0)
        pen.rt(30)

    # Draw The Hour Hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("white")
    pen.setheading(90)
    angle = (h / 12) * 360 + (m / 60) * 30
    pen.rt(angle)
    pen.pendown()
    pen.fd(70)

    # Draw The Minute Hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("red")
    pen.setheading(90)
    angle = (m / 60) * 360 + (s / 60) * 6
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    # Draw The Second Hand
    pen.penup()
    pen.goto(0, 0)
    pen.color("gold")
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(150)


while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))
    
    draw_clock(h, m, s, pen)
    wn.update()

    time.sleep(1)

    pen.clear()



wn.mainloop()
