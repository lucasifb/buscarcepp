
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/buscarcep')
def buscarcep():
    cep = request.args.get('cep')

    url_api = 'https://viacep.com.br/ws/' + cep + '/json/'
    response = requests.get(url_api)
    dados = response.json()

    endereco = dados.get("logradouro")
    bairro = dados.get("bairro")
    cidade = dados.get("localidade")
    estado = dados.get("uf")

    return render_template('index.html', cep=cep, endereco=endereco,
                           bairro=bairro, cidade=cidade, estado=estado)


if __name__ == '__main__':
    app.run(debug=True)







if __name__ == '__main__':
    app.run(debug=True)









