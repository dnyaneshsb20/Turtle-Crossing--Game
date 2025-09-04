import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

is_moving_up = False
game_is_on = True

def start_moving_up():
    global is_moving_up
    is_moving_up = True

def stop_moving_up():
    global is_moving_up
    is_moving_up = False

def restart_game():
    global game_is_on
    player.go_to_start()
    car_manager.reset()
    scoreboard.reset()
    game_is_on = True

screen.listen()
screen.onkeypress(start_moving_up, "Up")
screen.onkeyrelease(stop_moving_up, "Up")
screen.onkeypress(start_moving_up, "w")
screen.onkeyrelease(stop_moving_up, "w")
screen.onkey(restart_game, "r")

while True:
    screen.update()
    time.sleep(0.1)

    if game_is_on:
        if is_moving_up:
            player.go_up()

        car_manager.create_car()
        car_manager.move_cars()

        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_is_on = False
                scoreboard.game_over()

        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

screen.exitonclick()
