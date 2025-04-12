from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self, scr_width: int, scr_height: int):
        super().__init__()
        self.axis_x = scr_width / 2 - 20
        self.axis_y = scr_height / 2 - 20
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-self.axis_x, self.axis_x)
        random_y = random.randint(-self.axis_y, self.axis_y)
        self.goto(random_x, random_y) 
