from turtle import Turtle
ALIGNMENT="center"
FONT=('Courier', 16, 'bold')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,265)
        self.update_score()

    def update_score(self):
        self.write(f"score:{self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!!!touch screen to exit", align=ALIGNMENT, font=FONT)
        

    def sb(self):
        self.score+=1
        self.clear()
        self.update_score()



