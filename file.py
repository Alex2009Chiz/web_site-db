import json
from tkinter.font import names

from flask import Flask, render_template, request
import sqlite3

con = sqlite3.connect('Задание 1.db', check_same_thread=False)
cursor = con.cursor()

app = Flask(__name__)


@app.route('/0')
def medicines():
    cursor.execute('SELECT * FROM medicines')
    a = cursor.fetchall()
    return render_template('lol.html', medicines=a)


@app.route('/')
def find():
    return render_template('gol.html')


@app.route('/find_page/')
def find_page():
    name = request.args.get('name')
    cursor.execute('SELECT * FROM medicines WHERE name=(?)', [name])
    a = cursor.fetchall()

    print(a)
    return render_template('ff.html', medicines=a, name=name)


app.run(debug=True)
