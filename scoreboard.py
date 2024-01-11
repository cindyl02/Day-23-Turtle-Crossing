from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-250, 250)
        self.display_score()

    def increase_level(self):
        self.level += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
