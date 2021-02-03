from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")         # set background colour of screen
screen.title("Snake Game")
# All 3 turtles will scurry one behind the other
# tracer() turns on/off the animation, and the scurrying is not shown now
# tracer(0) means turn off the tracer
# To show the changes in turtle positions, update() is done periodically
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    # Shows only the current turtle positions, without showing the path they followed (animation)
    # update() resets and redraws the positions
    screen.update()
    time.sleep(0.1)
    scoreboard.manage_score()
    snake.move()

    # Detect collision of snake with food
    if snake.head.distance(food) < 15:          # food is 10 x 10 in size, so keeping buffer -> 15
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or \
            snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.turtles[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
