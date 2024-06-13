import sqlite3

# Função para criar a tabela de usuários no banco de dados
def criar_tabela():
    conn = sqlite3.connect('dbusers.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um novo usuário no banco de dados
def inserir_usuario(nome, email, senha):
    conn = sqlite3.connect('dbusers.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    conn.commit()
    conn.close()

# Função para buscar um usuário pelo ID
def buscar_usuario_por_id(usuario_id):
    conn = sqlite3.connect('dbusers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id=?', (usuario_id,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

# Função para atualizar os dados de um usuário
def atualizar_usuario(usuario_id, nome, email, senha):
    conn = sqlite3.connect('dbusers.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET nome=?, email=?, senha=? WHERE id=?', (nome, email, senha, usuario_id))
    conn.commit()
    conn.close()

# Função para buscar um usuário no banco de dados
def buscar_usuario(email, senha=None):
    conn = sqlite3.connect('dbusers.db')
    cursor = conn.cursor()
    if senha:
        cursor.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha))
    else:
        cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

# Função para excluir um usuário do banco de dados
def excluir_usuario(usuario_id):
    print("Excluindo usuário com ID:", usuario_id)
    conn = sqlite3.connect('dbusers.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=?', (usuario_id,))
    conn.commit()
    conn.close()
