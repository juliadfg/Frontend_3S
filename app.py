from flask import Flask, render_template, request, flash, redirect, url_for
from flask import Flask, render_template, url_for, flash, request
from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
# mover para .env

app.config['SECRET_KEY'] = '1234'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['form-email']
        senha = request.form['form-senha']

        if email and senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()

            if resultado_email:
                if resultado_email.check_password(senha):
                    login_user(resultado_email)
                    flash(f'Logado com sucesso!', 'sucess')
                    return redirect(url_for('index'))
                else:
                    flash('Senha incorreto!', 'danger')
                    return render_template('login.html')
            else:
                flash('Email não encontrado')
                return render_template('login.html')
        else:
            flash('Preencher os campos!', 'danger')
            return render_template('login.html')

    return render_template('login.html')

@app.route('/cadastro_funcionario', methods=['GET', 'POST'])
def cadastro_funcionario(MySQLchemyError=None):
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        email = request.form['email']
        if not nome or not senha or not email:
            flash('Preencher todos os campos!, danger')
            return render_template('cadastro.html')
        verificar_email = select(Funcionario).where(Funcionario.email == email)
        existe_email = db_session.execute(verificar_email).scalars_one_or_none()
        if existe_email:
            flash(f'Email {email} ja esta cadastrado!, danger')
            return render_template('cadastro.html')
        try:
            novo_func = Funcionario(nome=nome, email=email)
            novo_func.set_password(senha)
            db_session.add(novo_func)
            db_session.commit()
            flash(f'Funcionario {nome} cadastrado com sucesso!', 'sucess')
            return redirect(url_for('login'))
        except MySQLchemyError as e:
            flash(f'Erro na base de dados ao cadastrar!', 'danger')
            print(f'Erro na base de dados ao cadastrar!')
            return redirect(url_for('cadastro_funcionario'))
        except Exception as e:
            flash(f'Erro ao cadastrar!', 'danger')
            print(f'Erro ao cadastrar usuario!')
            return redirect(url_for('cadastro_funcionario'))
    return render_template('cadastro.html')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/funcionarios', methods=['GET', 'POST'])
def funcionarios():
    funcionarios_sql = select(Funcionario)
    funcionarios_resultado = db_session.execute(funcionarios_sql).scalars().all()
    return render_template("funcionarios.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")
@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            flash("Preencha o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/subtracao', methods=['GET', 'POST'])
def subtracao():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtracao = n1 - n2
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, subtracao=subtracao)
        else:
            flash("Preencha o campo para realizar a subtração", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            multiplicar = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
        else:
            flash("Preencha o campo para realizar a multiplicação", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            dividir = n1 / n2
            flash("Sucesso", 'alert-success')
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)
        else:
            flash("Preencha o campo para realizar a divisão", 'alert-danger')

    return render_template("operacoes.html")

@app.route('/triangulo_perimetro', methods=['GET', 'POST'])
def triangulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n1'] :
            n1 = int(request.form['form-n1'])
            n2 = 3
            triangulo_perimetro = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=3, triangulo_perimetro=triangulo_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/triangulo_area', methods=['GET', 'POST'])
def triangulo_area():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            n3= 2
            triangulo_area = n1 * n2 / n3
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, n3=2, triangulo_area=triangulo_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/circulo_perimetro', methods=['GET', 'POST'])
def circulo_perimetro():
    if request.method == 'POST':
        if request.form['form-n9']:
            n7 = 2
            n8 = 3.14
            n9= int(request.form['form-n9'])
            circulo_perimetro = n7 * n8 * n9
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n7=2, n8=3.14, n9=n9, circulo_perimetro=circulo_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/circulo_area', methods=['GET', 'POST'])
def circulo_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1= int(request.form['form-n1'])
            circulo_area = 3.14 * n1 * n1
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, circulo_area=circulo_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/quadrado_perimetro', methods=['GET', 'POST'])
def quadrado_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            n2 = 4
            quadrado_perimetro = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=4, quadrado_perimetro=quadrado_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")
@app.route('/quadrado_area', methods=['GET', 'POST'])
def quadrado_area():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            quadrado_area = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=n2, quadrado_area=quadrado_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/hexagono_perimetro', methods=['GET', 'POST'])
def hexagono_perimetro():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            n2 = 6
            hexagono_perimetro = n1 * n2
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=6, hexagono_perimetro=hexagono_perimetro)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route('/hexagono_area', methods=['GET', 'POST'])
def hexagono_area():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            n2 = 6
            n4 = 4
            n3 = 1.7
            hexagono_area = n2 * n1 * n1 * n3 / n4
            flash("Sucesso", 'alert-success')
            return render_template("geometria.html", n1=n1, n2=6, n3=1.7, n4=4, hexagono_area=hexagono_area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')

    return render_template("geometria.html")

@app.route("/logout")
def logout():
    logout_user()
    flash("Logout sucesso", 'alert-success')
    return redirect(url_for("login"))

# TODO Final do código

if __name__ == '__main__':
    app.run(debug=True)