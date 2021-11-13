import time
from turtle import Turtle, Screen
from car_manager import CarManager
from player import Player
from scorebord import ScoreBoard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

game_on = True

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()


screen.onkeypress(player.move_forward, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # Successful Crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
