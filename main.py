import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player_1 = Player()
car_manager = CarManager()
score = Scoreboard()
screen.onkey(player_1.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    if player_1.ycor() > 280:
        player_1.restart()
        score.level_up()
        car_manager.move_increment()

    # turtle collides with car "squish"
    for squish in car_manager.all_cars:
        if squish.distance(player_1) < 20:
            game_is_on = False
            score.game_over()

screen.exitonclick()
