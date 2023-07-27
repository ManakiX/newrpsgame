from flask import Flask, render_template, request
import random

app = Flask(__name__)

def get_choices():
    player_choice = request.form['choice']
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors. You win!'
        else: 
            return 'Paper covers rock. You lose.'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock. You win!'
        else: 
            return 'Scissors cuts paper. You lose.'
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts paper. You win!'
        else: 
            return 'Rock smashes scissors. You lose.'

@app.route('/', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        choices = get_choices()
        result = check_win(choices['player'], choices['computer'])
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
