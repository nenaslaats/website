# -*- coding: utf-8 -*-
"""
Created on Tue May 12 18:00:14 2020

@author: nenas
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)