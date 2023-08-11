from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=800, height=680)  # x-> -400, +400   y -> 340, -340
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # turns off the turtle animations

# constructing objects from the classes
snake = Snake()
food = Food()
score = Score()

screen.listen()  # listens for the events of keyboard clicks

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True


def when_game_end():
    """ To check for highest score and ask for winner name and , then asks for game replay"""
    score.game_over()  # display Game Over

    if score.current_score > score.highest_score:
        # congrats highest scorer in display screen
        score.winner_greeting()
        winner_name = screen.textinput(title="Highest scorer!", prompt="what's your first name:").lower()

        # at the same time  display the name of the winner and the highest score together
        score.ask_for_winner(winner_name)
        score.game_over()

    play_again = screen.textinput(title="Game Over", prompt="wanna play again? 'y' or 'n':  ").lower()
    if play_again != "n":
        screen.listen()
        score.reset_score()
        snake.reset_snake()
    else:
        # how to remove a text from the screen ?
        score.game_over()
        global game_on
        game_on = False


while game_on:
    screen.update()  # updates the screen after each modification, only works when screen.tracer is on
    time.sleep(0.1)  # delay the screen refresh
    snake.move()

    # ---------- How to detect collision with food and generate random food----------------
    if snake.head.distance(food) < 15:  # if distance between head and food
        food.move_food_randomly()
        # print("nom nom nom")
        score.add_score()
        snake.increase_tail()

    # ------------ checks for game-ends and then show "Game-Over" on screen and ask for game continue----------

    # Detect collision with the wall
    if snake.head.xcor() < -400 or snake.head.xcor() > 399 or snake.head.ycor() < - 337 or snake.head.ycor() > 340:
        when_game_end()

    # How to detect collision with the tail
    for i in snake.segments:
        if snake.head.distance(i) < 10 and i != snake.segments[0]:  # but not for snake head itself
            when_game_end()

screen.exitonclick()
