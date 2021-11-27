from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

    def level_score(self, level):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-280, 255)
        self.write(f"Level {level}", align="left", font=FONT)

    def game_over(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
