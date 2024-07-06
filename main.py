#!/usr/bin/python3
#Author: IMr Code

from flask import Flask, render_template, request
from flask import url_for, redirect
import openpyxl

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():

    file = request.files['arquivo']

    if file == '' or file == None:
        return 'Invalid archive'

    file.save("./arquivos/{}".format(file.filename))

    workbook = openpyxl.load_workbook("./arquivos/{}".format(file.filename))
    sheet = workbook.active

    coluna1 = [ ]
    coluna2 = [ ]

    for a, b in zip(sheet['A'], sheet['B']):
        coluna1.append(a.value)
        coluna2.append(b.value)

    dados = list(zip(coluna1, coluna2))

    print('DADOS')
    print(dados)

    return render_template('resultado.html',dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
