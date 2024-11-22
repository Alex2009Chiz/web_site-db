import json
from tkinter.font import names

from flask import Flask, render_template, request
import sqlite3

con = sqlite3.connect('Задание 1.db', check_same_thread=False)
cursor = con.cursor()

app = Flask(__name__)


@app.route('/')
def medicines():
    cursor.execute('SELECT * FROM medicines')
    a = cursor.fetchall()
    return render_template('lol.html', medicines=a)


@app.route('/0')
def find():

    return render_template('get_db.html')

@app.route('/save_db/')
def save_db():
    name = request.args.get('name')
    manufacturer = request.args.get('manufacturer')
    forma = request.args.get('forma')
    price = request.args.get('price')
    id = request.args.get('id')
    print(name,manufacturer)
    cursor.execute('INSERT INTO medicines (name,manufacturer,form,price,id) VALUES(?,?,?,?,?)' ,(name,manufacturer,forma,price,id))
    con.commit()
    return 'ok'

@app.route('/find_page/')
def find_page():

    type_find = request.args.get('type_find')
    text = request.args.get('name')

    cursor.execute(f'SELECT * FROM medicines WHERE {type_find}=(?)', [text])
    a = cursor.fetchall()
    print(a)
    return render_template('ff.html', medicines=a)







app.run(debug=True)
