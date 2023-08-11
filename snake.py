from turtle import Turtle

MOVE_DISTANCE = 20  # snake goes forward 20 paces  everytime

UP = 90  # directions
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(-20, 0), (-40, 0), (-60, 0)]  # .positions() returns a tuple of x, y


class Snake:
    def __init__(self):
        self.segments = []  # it only contains turtle objects
        self.create()
        self.head = self.segments[0]  # the mouth of snake

    def structure(self, position):
        """ How the snake will look like and its origin place"""
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(position)
        self.segments.append(tim)

    def create(self):
        """ creates 3 instances of snake objects and appends into a list"""  # 👆
        for position in STARTING_POSITIONS:
            self.structure(position)

    def increase_tail(self):
        """ If snake eats food then we create a new turtle object and append it the end of the segments list"""
        self.structure(self.segments[-1].position())  # wherever it is on screen
        # print(f"RANGE LIST: {len(self.segments)}")

    def move(self):
        """ It will make the snake move by looping through from last value to first one , like 3->2->1 -> forward"""
        for seg in range(len(self.segments) - 1, 0, -1):  # (start, stop, step)
            new_position = self.segments[seg - 1].position()  # returns a tuple(xcor, ycor)
            self.segments[seg].goto(new_position[0], new_position[1])
        self.head.forward(20)

    def reset_snake(self):
        """ resets the snake to only 3 initial segments """
        for i in self.segments:   # remove every turtle class from the segments i.e, the body of the snake
            i.goto(x=-9000, y=9000)  # send all to somewhere off-screen, what about Big screen ???

        self.segments.clear()  # Remove all items from list.
        self.create()  # create a  new 3 turtles from the beginning
        self.head = self.segments[0]

    def up(self):
        """ Get hold of 1st square from the segments list and give it a direction, and rest will follow"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        #                 👇 always use () at last, or else it will never give any value
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
