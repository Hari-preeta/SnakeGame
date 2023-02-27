from turtle import Turtle

POSITION = [(0,0),(-20,0),(-40,0)]
MOVE=20
UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_turtles=[]
        self.Create_snake()
        self.head=self.all_turtles[0]


    def Create_snake(self):
        for turtle_position in POSITION:
            self.add_snake(turtle_position)

    def add_snake(self,turtle_position):
        new_turtle = Turtle("circle")
        new_turtle.color("red")
        new_turtle.penup()
        new_turtle.goto(turtle_position)
        self.all_turtles.append(new_turtle)

    def snake_extend(self):
        self.add_snake(self.all_turtles[-1].position())



    def move(self):
        for seg_num in range(len(self.all_turtles)-1,0,-1):
            x = self.all_turtles[seg_num - 1].xcor()
            y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(x,y)
        self.head.forward(MOVE)


    def rt(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def lt(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def dw(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
















































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
#
# game_is_on=True
# while game_is_on:
#     s.update()
#     time.sleep(0.1)
#     for seg_num in range(len(all_turtles)-1,0,-1):
#         x = all_turtles[seg_num - 1].xcor()
#         y = all_turtles[seg_num - 1].ycor()
#         all_turtles[seg_num].goto(x,y)
#     all_turtles[0].forward(20)
#     all_turtles[0].left(90)

