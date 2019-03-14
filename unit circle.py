from turtle import Turtle, Screen
from sys import exit
#works pretty good, fix the way you can select it, or:
#if you drag too close to the center, the lines don't show up properly (cosine [t4], sine [t3]), so stay a good distance out

#add tangent?

def write():
    side = 1
    t2.goto(-450, 300)
    
    t2.color("red")
    t2.write("Radius: 1", False, align="left",font=("Arial",  15, "normal"))
    #rad
    
    t2.goto(-450, 250)
    
    
    

    t2.write("Angle from North: " + str(t.heading())[0:9], False, align="left",font=("Arial",  15, "normal"))
    if t.heading() >= 180:
        side = -1
    t2.goto(-450, 200)
    if t.heading() >= 90:
        t2.write("Angle: " + str(abs(360 - t.heading() + 90))[0:9], False, align="left",font=("Arial",  15, "normal"))
    else:
        t2.write("Angle: " + str(abs(t.heading() - 90))[0:9], False, align="left",font=("Arial",  15, "normal"))
    #write sin
    t2.color("blue")
    
    
    t2.goto(-450, 150)
    t2.write("Length of Cosine: " + str(t4.distance(0,t3.xcor())/t.shapesize()[1]/2/10 * side)[0:9], False, align="left",font=("Arial",  15, "normal"))
    #write cos
    t2.color("green")
    t2.goto(-450, 100)
    t2.write("Length of Sine: " + str(t3.distance(t3.xcor(), 0) / t.shapesize()[1] / 2 / 10 * side)[0:9], False, align="left",font=("Arial",  15, "normal"))
    s.update()
    
    #s.ontimer(write, 1)
    
    
def quit():
    s.bye()
    exit(0)
    
def create():
    
    
    global rad
    t.color("black", "black")
    t.shapesize(0.4)
    t.stamp()
    t.color("black", "")
    t.shapesize(20, 20, 3)
    t.stamp()
    t.shape("hand")
    #t.goto(t.xcor(), t.ycor() + 100)
    t.shapesize(.1, 10)
    t.color("red") 
    t3.seth(t3.heading() + 90)
    t3.goto(0,0)
    t3.color('green')
    #t.forward(100)
    t.goto(0,100)
    t2.goto(-400, 300)
    s.update()
    
    t4.goto(0,0)
    t3.goto(0,0)
    #print(t.shapesize())
    
def drag(x,y):
    if t4.distance(x,y) > 109:
        tt = t.towards(x,y)
        t3.goto(t.pos())
        if t3.distance(0,0) / t.shapesize()[1] < 1:
            tt = 360 - t.towards(x,y)
        t3.setheading(tt)
        t3.forward(100)
        if t.heading() <= 90 or t.heading() > 270:
            t3.setheading(90)
        elif t.heading() > 90 and t.heading() <= 270:
            t3.setheading(-90)
            
        
        #print(t4.distance(x,y))
        t4.st()
        t3.st()
        
        t.goto(0,0) #sin, cosine of circle * 100?
        t.setheading(t.towards(x,y))
        t.forward(100)
        
        
        #t3.dot()
        if t.heading() >= 180:
            t4.setheading(180)
        else:
            t4.setheading(0)
        t3.shapesize(t3.distance(t3.xcor(), 0) / t.shapesize()[1] / 2 , .1)
        t4.shapesize(t4.distance(0,t3.xcor())/t.shapesize()[1]/2, .1)
    
    
    #print(t.towards(x,y))
    
    
    
    
   # t4.seth(0)
    
    s.update()
    
    
    
def release(x,y):
    write()

def erase(x,y):
    t2.clear()

s = Screen()    
s.mode("logo")
t = Turtle("circle", visible=True)
t2 = Turtle("square", visible=False)
t3 = Turtle("square", visible=False)
t4 = Turtle("square", visible=True)
trat = 0
t4.color("blue")
print(t3.get_shapepoly())
t3.shapesize(10,.1)
print(t3.get_shapepoly())
t4.shapesize(10,.1)
t4.penup()
t2.penup()
v = 0
t3.color("blue")
s.tracer(False)
s.listen()
s.onkeypress(quit, "Escape")


t.penup()
t3.penup()
s.register_shape("hand", ((0,-10), (0,10), (20,10), (20, -10)))
t4.shape("hand")
t3.shape("hand")

create()
write()
t.onclick(erase)
t.ondrag(drag)
t.onrelease(release)

s.mainloop()