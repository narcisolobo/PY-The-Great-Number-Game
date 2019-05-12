from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'is it great really'

import random

@app.route('/')
def index():
    session['computer_num'] = random.randint(1, 100)
    session['num_attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['num_attempts'] += 1
    session['human_guess'] = int(request.form['human_guess'])
    session['less_than'] = False
    session['greater_than'] = False
    session['exactly'] = False
    if session['human_guess'] < session['computer_num']:
        session['less_than'] = True
    elif session['human_guess'] > session['computer_num']:
        session['greater_than']  = True
    elif session['human_guess'] == session['computer_num']:
        session['exactly'] = True
    return redirect('/showguess')

@app.route('/showguess')
def showguess():
    return render_template('guess.html', less_than=session['less_than'], greater_than=session['greater_than'], exactly=session['exactly'], human_guess=session['human_guess'], computer_num=session['computer_num'], num_attempts=session['num_attempts'])

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)