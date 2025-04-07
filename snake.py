import turtle
from encodings.punycode import segregate
from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()
screen.listen()

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            seg = Turtle('square')
            seg.color('white')
            seg.penup()
            seg.goto(position)
            self.segments.append(seg)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



#
# def move():
#     play_game = True
#     while play_game:
#         screen.update()
#         time.sleep(0.05)
#         for seg_num in range(len(segments) - 1,0,-1):
#             new_x = segments[seg_num - 1].xcor()
#             new_y = segments[seg_num - 1].ycor()
#             segments[seg_num].goto(new_x, new_y)
#         segments[0].forward(20)
#         def turn_right():
#             segments[0].right(90)
#         def turn_left():
#             segments[0].left(90)
#         # screen.onkey(key='Left', fun=turn_left)
#         # screen.onkey(key='Right', fun=turn_right)
#
#         if segments[0].xcor() > 280 or segments[0].xcor() < -280:
#             play_game = False
#             screen.bye()
#

