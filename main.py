# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
from sklearn.linear_model import LinearRegression
from googletrans import Translator
import pickle

colunas = ['tamanho', 'ano', 'garagem']
modelo = pickle.load(open('modelo.sav', 'rb'))



app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'nome'
app.config['BASIC_AUTH_PASSWORD'] = '123456'

basic_auth = BasicAuth(app)
translator = Translator()

@app.route('/')
def home():
    return 'Olá, mundo!'

@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = translator.translate(str(tb), src='pt', dest='en')
    tb_en_blob = TextBlob(tb_en.text)
    polaridade = tb_en_blob.sentiment.polarity
    return 'A polaridade da frase é: {}'.format(polaridade)

@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([[dados_input]])
    return jsonify(preco=preco[0])


app.run(debug=True)