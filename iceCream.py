import turtle as t
t.speed("fastest")

t.penup()
t.goto(160,200)
t.pendown()


t.pencolor("black")
t.fillcolor("brown")
t.begin_fill()
t.left(50)
t.circle(200,260)
t.left(50)
t.fd(300)
t.end_fill()

t.fillcolor("gold")
t.begin_fill()
t.right(100)
t.fd(800)
t.right(158)
t.fd(800)
t.end_fill()

t.fillcolor("brown")
t.begin_fill()
t.backward(100)
t.right(120)
t.fd(265)
t.right(80)
t.fd(50)
t.right(100)
t.fd(246)
t.end_fill()

t.fillcolor("brown")
t.begin_fill()
t.left(120)
t.fd(200)
t.left(60)
t.fd(170)
t.right(82)
t.fd(50)
t.right(100)
t.fd(160)
t.end_fill()

t.penup()
t.goto(160,350)
t.pendown()

t.right(160)
t.fillcolor("pink")
t.begin_fill()
t.left(50)
t.circle(200,260)
t.left(50)
t.circle(40,90)
t.right(180)
t.circle(40,180)
t.right(180)
t.circle(40,180)
t.right(180)
t.circle(40,180)
t.right(180)
t.circle(40,100)
t.end_fill()

t.penup()
t.goto(100,550)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(10,500)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-100,550)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-50,450)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(50,450)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(20)
t.end_fill()


t.done()
