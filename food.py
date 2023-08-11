from turtle import Turtle
import random


class Food(Turtle):  # using class Inheritance i,e  the Food class has properties of Turtle class too
    def __init__(self):
        super().__init__()
        self.food_design()

    def food_design(self):
        """ how the food will appear"""
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.shapesize(0.7)
        self.speed(0)
        self.move_food_randomly()

    def move_food_randomly(self):
        """ randomly choose the x and y value if snake eats the previous food """

        random_x = random.randint(-373, 373)
        random_y = random.randint(-308, 308)
        # print(f"random X = {random_x} \n  Y : {random_y}")
        self.goto(x=random_x, y=random_y)
