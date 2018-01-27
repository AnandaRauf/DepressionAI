from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_session()
    welcome_text = render_template('')
    welcome_re_text = render_template('welcome_re')

    return question(welcome_text).reprompt(welcome_re_text)

