import turtle
import time
from snake import Snake

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()

is_game_started = True

while is_game_started:
    snake.move()
    screen.update()
    time.sleep(0.1)


screen.exitonclick()

