from flask import Flask, render_template, request
from utils.bibliotecaswm import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    cadeia = request.form['vetor'].replace(" ", "")
    operacao = request.form['operacao']

    vetor1, vetor2 = atribuir_vetores(cadeia)

    try:
        if operacao == "somar":
            resultado = somar_vetores(vetor1, vetor2)
        elif operacao == "subtrair":
            resultado = diferenca_vetores(vetor1, vetor2)
        elif operacao == "produto_escalar":
            resultado = produto_escalar(vetor1, vetor2)
        elif operacao == "norma":
            resultado = norma(vetor1)
        elif operacao == "vetor_unitario":
            resultado = vetor_unitario(vetor1)
        elif operacao == "produto_vetorial":
            resultado = produto_vetorial(vetor1, vetor2)
        elif operacao == "projecao_vetorial":
            resultado = projecaovetorial_vetor1_sobre_vetor2(vetor1, vetor2)
        elif operacao == "ortogonalizacao":
            resultado = ortogonalizacao_gram_schmidt([vetor1, vetor2])
        else:
            resultado = "Operacao inválida"
    except Exception as e:
        resultado = f"Errp: {e}"

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
