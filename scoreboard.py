from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("user_data/highestScore.txt", mode="r") as file:
            self.highest_score = int(file.read())

        with open("user_data/winner.txt", mode="r") as file:
            self.highest_scorer_name = file.read()

        self.hideturtle()
        self.penup()
        self.pencolor("cyan")
        self.display()

    def display(self):
        """ Displays the current score on top"""
        self.clear()

        self.goto(x=0, y=300)
        self.write(f"Score: {self.current_score}     High Score: {self.highest_score} by {self.highest_scorer_name} ",
                   align='center', font=('Courier', 18, 'normal'))  # updated each time

    def add_score(self):
        """ adds 1 points each time the snake eats the food """
        self.current_score += 1
        self.display()

    def game_over(self):
        """ when game will end, only then shows game over """
        self.goto(x=0, y=80)
        self.pencolor("red")
        self.write("Game Over", align='center', font=('Courier', 26, 'normal'))

    def ask_for_winner(self, winner_name):
        """asks for game winner name, if score is highest and also updates the highest score"""
        self.highest_scorer_name = winner_name
        with open("user_data/winner.txt", mode="w") as file:
            file.write(winner_name)
        if self.current_score > self.highest_score:  # to quickly update the highest score ONLY for better UI
            self.highest_score = self.current_score
            with open("user_data/highestScore.txt", mode="w") as file:
                file.write(str(self.current_score))
        self.pencolor("limegreen")
        self.display()

    def reset_score(self):
        """ as new game starts, set current_score -> 0 """
        # self.score = 0  -> if made score -> 0, then highest_score is also 0 and will never change
        self.pencolor("cyan")  # from red color of game-over -> to again cyan
        self.current_score = 0
        self.display()

    def winner_greeting(self):
        """ if the player made a new highest record, so for greeting"""
        self.goto(x=0, y=160)
        self.pencolor("magenta")
        self.write("Congratulations! \n You've set a new highest record \n", align='center',
                   font=('Courier', 20, 'normal'))
