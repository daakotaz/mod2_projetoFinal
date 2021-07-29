from flask import Flask,render_template,request,session,flash,redirect,url_for

app = Flask(__name__)
app.secret_key = 'BlueEdTech'

class Cliente:
    def __init__(self,nome,email,senha,pagamento):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pagamento = pagamento

class Hamburgueria():
    def __init__(self):
        self.clientes_cadastrados = {}
    
    def cadastrar_cliente(self,cliente):
        self.clientes_cadastrados[cliente.email] = cliente.senha

hamburgueria = Hamburgueria()




@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

@app.route('/cliente',methods=['POST',])
def cliente():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    pagamento = request.form['pagamento']

    cliente = Cliente(nome,email,senha,pagamento)
    hamburgueria.cadastrar_cliente(cliente)
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar',methods=['POST',])
def autenticar():
    if request.form['email'] not in hamburgueria.clientes_cadastrados.keys():
        flash('Cadastro não realizado')
        return redirect(url_for('cadastrar'))

    elif request.form['senha'] not in hamburgueria.clientes_cadastrados.values():
        flash('Login não realizado')
        return redirect(url_for('login'))
        
    else:
        session['usuario_logado'] = request.form['email']
        flash('Login realizado com sucesso!')
        return redirect(url_for('menu'))

@app.route('/menu')
def menu():
    return render_template('menu.html')
        


if __name__ == '__main__':
    app.run(debug=True)