import random
from turtle import Turtle, Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40,0)]
MOVE_DIS = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ["pink", "cyan", "orange", "yellow", "red", "violet", "green"]
class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()

        self.head= self.segments[0]


    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            pos_x = self.segments[seg - 1].xcor()
            pos_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(pos_x, pos_y)
        self.head.forward(MOVE_DIS)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("cyan")
        # new_segment.speed("fast")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for snake in self.segments:
            snake.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:

            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)