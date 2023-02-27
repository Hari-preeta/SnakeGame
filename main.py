from turtle import Screen , Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

tim=Turtle()
sn=Snake()
fd=Food()
s=Screen()
sc=Score()
s.setup(width=600,height=600)
s.title("snake game")
s.bgcolor("black")
s.tracer(0)
xy_pd=285
xy_nd=-285


s.listen()
s.onkey(key="Right", fun=sn.rt)
s.onkey(key="Left", fun=sn.lt)
s.onkey(key="Up", fun=sn.up)
s.onkey(key="Down", fun=sn.dw)



game_is_on=True
while game_is_on:
    s.update()
    time.sleep(0.1)
    sn.move()
    #detect collision
    if sn.head.distance(fd) < 15:
        print("nom nom nom")
        sn.snake_extend()
        sc.sb()
        fd.refresh()

    if sn.head.xcor() > xy_pd or sn.head.xcor() < xy_nd or sn.head.ycor() > xy_pd or sn.head.ycor() < xy_nd:
        sc.game_over()
        game_is_on = False

    for segment in sn.all_turtles[2:]:

        # if segment == sn.head:
        #     pass

        if sn.head.distance(segment) < 8:
            sc.game_over()
            game_is_on = False



s.exitonclick()






























# position=[(0,0),(-20,0),(-40,0)]
# all_turtles=[]
#
#
# for turtle_position in position:
#     new_turtle=Turtle("square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(turtle_position)
#     all_turtles.append(new_turtle)

# game_is_on=True
# while game_is_on:
#     s.update()
#     time.sleep(0.1)
#     sn.move(20)
    # for seg_num in range(len(all_turtles)-1,0,-1):
    #     x = all_turtles[seg_num - 1].xcor()
    #     y = all_turtles[seg_num - 1].ycor()
    #     all_turtles[seg_num].goto(x,y)
    # all_turtles[0].forward(20)
    # all_turtles[0].left(90)

