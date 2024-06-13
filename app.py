
import logging
import sqlite3
import espelhodbtxt

from flask import Flask, render_template, request, redirect, url_for
from conexao import atualizar_usuario, buscar_usuario_por_id, criar_tabela, inserir_usuario, buscar_usuario, excluir_usuario

app = Flask(__name__)

# Rota para a página de login
@app.route('/')
def login():
    return render_template('login.html')


# Rota para a página de cadastro de usuário
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        inserir_usuario(nome, email, senha)
        return redirect(url_for('login'))
    return render_template('cadast_user.html')

# Rota para a página de cadastro de usuário
# @app.route('/cadastro')
# def cadastro():
#    return render_template('cadast_user.html')

# Rota para a página de conteúdo
@app.route('/conteudo')
def conteudo():
    # Busca todos os usuários cadastrados
    usuarios = buscar_usuario(email=None)
    return render_template('conteudo.html', usuarios=usuarios)

# Rota para a página de conteúdo
#@app.route('/conteudo')
#def conteudo():
 #   # Busca todos os usuários cadastrados
 #   usuarios = buscar_usuario()
 #   return render_template('conteudo.html', usuarios=usuarios)

# Rota para o processo de login
@app.route('/login', methods=['POST'])
def fazer_login():
    email = request.form['email']
    senha = request.form['senha']
    usuario = buscar_usuario(email, senha)
    if usuario:
        return redirect(url_for('conteudo'))
    else:
        return "Usuário não encontrado."

# Rota para edição de registro
@app.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
def editar(usuario_id):
    usuario = buscar_usuario_por_id(usuario_id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        atualizar_usuario(usuario_id, nome, email, senha)
        return redirect(url_for('conteudo'))
    return render_template('editreg.html', usuario_id=usuario_id, usuario=usuario)

# Rota para exclusão de registro
@app.route('/excluir/<int:usuario_id>', methods=['DELETE'])
def excluir(usuario_id):
    excluir_usuario(usuario_id)
    return redirect(url_for('conteudo'))


if __name__ == '__main__':
    # Criação da tabela de usuários no banco de dados, se ainda não existir
    criar_tabela()
    # Inicialização do servidor
    app.run(debug=True)



# Configuração do logger
logging.basicConfig(filename='database.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Função para adicionar um novo usuário ao banco de dados
def adicionar_usuario(nome, email, senha):
    # Lógica para adicionar usuário ao banco de dados
    logging.info(f'Novo usuário adicionado: Nome={nome}, Email={email}')

# Função para editar um usuário existente no banco de dados
def editar_usuario(nome, email, nova_senha):
    # Lógica para editar usuário no banco de dados
    logging.info(f'Usuário editado: Nome={nome}, Novo Email={email}, Nova Senha={nova_senha}')

# Função para excluir um usuário do banco de dados
def excluir_usuario(email):
    # Lógica para excluir usuário do banco de dados
    logging.info(f'Usuário excluído: Email={email}')

# Exemplos de uso das funções
adicionar_usuario('João', 'joao@example.com', '123456')
editar_usuario('João', 'joao@example.com', 'novasenha123')
excluir_usuario('joao@example.com')