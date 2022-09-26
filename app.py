from flask import Flask, redirect, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPTS'] = False
app.config['SECRET_KEY'] = 'secretBoggLe123'

debug = DebugToolbarExtension(app)



boggle_game = Boggle()

@app.route('/', methods=['GET'])
def get_board():
    '''Render Boggle board and add it to the session'''

    board = boggle_game.make_board()

    session['BOARD'] = board

    return render_template('boggle_game.html', board=board)

    
