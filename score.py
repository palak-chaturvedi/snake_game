from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        with open('score.txt') as f:
            self.high_score = f.read()
            self.high_score = int(self.high_score)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=("Calibre", 10, "bold"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score= self.score
            with open("score.txt", "w") as f:
                f.write(f"{self.high_score}")

        self.score=0
        self.update()


    def upgrade(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game is OVER !!!", align="center", font=("Calibre", 10, "bold"))

