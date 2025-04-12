from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


screen = Screen()
scr_width = 600
scr_height = 600
screen.setup(scr_width, scr_height)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)

snake = Snake()
food = Food(scr_width, scr_height)
scoreboard = ScoreBoard(scr_height / 2 - 30)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # collision with wall
    if snake.head.xcor() > scr_width / 2 - 10 or snake.head.xcor() < -(scr_width / 2 - 10) or snake.head.ycor() > scr_height / 2 - 10 or snake.head.ycor() < -(scr_height / 2 - 10):
        scoreboard.game_over()
        break

    # collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
