from flask import Flask, request, make_response


app = Flask(__name__)


@app.route("/")
def homepage():
    return "Site no ar"

#  Cria uma informação de um usuario e salva no cookie do site
@app.route("/criar-cookie")
def criar_cookie():
    resposta = make_response("O cookie foi criado")
    resposta.set_cookie("nome_usuario","Hick")
    resposta.set_cookie("Idade","26")
    resposta.set_cookie("Email","hick.@gmail.com")
    resposta.set_cookie("Telefone","11xxxxx-xxxx")
    return resposta

# Com essa rota é possivel vizualizar os cookies criados em forma de lista 
@app.route("/ver-cookie")
def ver_cookie():
    cookies = request.cookies
    return cookies


if __name__ == "__main__":
    app.run(debug=True)