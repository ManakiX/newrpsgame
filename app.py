from flask import Flask, render_template, request
import random
import socket

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

def find_available_port(start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result != 0:  
            return port
        sock.close()
    return None

@app.route('/', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        choices = get_choices()
        result = check_win(choices['player'], choices['computer'])
        return render_template('index.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    available_port = find_available_port(8000, 8080) 
    if available_port:
        app.run(host='0.0.0.0', port=available_port)
    else:
        print("No available ports were found")