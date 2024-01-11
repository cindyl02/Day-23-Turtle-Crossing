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

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.add_car()
    car_manager.move_cars()
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.end_game()
    if player.is_at_finish_line():
        car_manager.level_up()
        player.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()
