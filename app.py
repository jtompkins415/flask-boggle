from flask import Flask, redirect, render_template, session, request, jsonify 
from flask_debugtoolbar import DebugToolbarExtension
from boggle import Boggle

app = Flask(__name__)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = 'secretBoggLe123'

debug = DebugToolbarExtension(app)



boggle_game = Boggle()

@app.route('/', methods=['GET'])
def go_to_board():
    '''Redirect to new board'''

    return redirect('/boggle')

@app.route('/boggle', methods=['GET'])
def get_board():
    '''Render Boggle board and add it to the session'''

    board = boggle_game.make_board()

    session['BOARD'] = board

    return render_template('boggle_game.html', board=board)


@app.route('/', methods=['POST'])
def check_word():
    '''Handles form submission and confirms if submitted word is valid'''

    guess_word = request.args['user_guess']
    board = session['BOARD']

    resp = boggle_game.check_valid_word(board, guess_word)

    return jsonify({'result': resp})
