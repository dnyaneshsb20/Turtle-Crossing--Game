from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_spawn_chance = 6  # Less = more cars per level

    def create_car(self):
        if random.randint(1, self.car_spawn_chance) == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.car_spawn_chance > 2:
            self.car_spawn_chance -= 1

    def reset(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_spawn_chance = 6
