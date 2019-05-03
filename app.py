from src import app
from flask import render_template
import os
from itsdangerous import URLSafeTimedSerializer

@app.route('/')
def index():
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True)

