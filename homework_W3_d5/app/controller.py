from app import app
from flask import render_template, request

from app.models.game import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='RPS')

@app.route('/play_game', methods=['POST'])
def play_game():
    player1 = Player('Mark', None)
    player2 = Player('Rob', None)
    player1.selection = request.form['selection1']
    player2.selection = request.form['selection2']
    result = Game.who_won(player1, player2)
    return render_template('rockpaperscissors.html', outcome=result, title='RPS Game' )
