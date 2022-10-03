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
    session['board'] = board
    highscore = session.get('highscore', 0)
    nplays = session.get('nplays', 0)

    session['board'] = board

    return render_template('base.html', board=board, highscore=highscore, nplays=nplays)


@app.route('/', methods=['POST'])
def check_word():
    '''Handles form submission and confirms if submitted word is valid'''

    guess_word = request.args['word']
    board = session['board']

    resp = boggle_game.check_valid_word(board, guess_word)

    return jsonify({'result': resp})

@app.route('/post-score', methods=['POST'])
def score_board():
    '''Handles score tracking'''

    score = request.json['score']
    highscore = session.get('highscore', 0)
    nplays = session.get('nplays', 0)

    session['nplays'] = nplays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokenrecored = score > highscore)