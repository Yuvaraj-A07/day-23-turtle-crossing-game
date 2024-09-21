COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move = STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_chance = random.randint(1, 6)
        if rand_chance == 1:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color(random.choice(COLORS))
            new_turtle.shapesize(stretch_wid=1, stretch_len=2)
            new_turtle.penup()
            rand_y = random.randint(-250, 250)
            new_turtle.goto(300, rand_y)
            self.all_cars.append(new_turtle)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move)

    def move_increment(self):
        self.move += 10
