from flask import Flask, render_template, session, redirect, url_for, escape, request, make_response, flash
import forms
#from flask_wtf.csrf import CSRFProtect
#from flask_mysqldb import MySQL

# Initialization
app = Flask(__name__)

# Settings sessions memory app
app.secret_key = "my_secret_key"
#csrf = CSRFProtect(app)


# Database


#MIDDLEWARES


# ROUTER
@app.route("/")
def halo():
    comment_form = forms.RegisterUser()
    return render_template('index.html', form = comment_form)


@app.route("/login", methods=['GET', 'POST'])
def login(title='parrafotest'):
    login_form = forms.LoginUser(request.form)

    if request.method == 'POST':
        print (login_form.username.data)
        print (login_form.email.data)
        print(login_form.password.data)

    return render_template('login.html', title=title, form = login_form)


#http://127.0.0.1:9000/params?params1=Eduardo&params2=Pepe
@app.route("/params/")
@app.route("/params/<user>/<int:id>")
def params(user = "no hay valor", id = "no"):
    params1 = request.args.get('params1', '1 no contiene parametros')
    return "El parametro es: {} {} ".format(user, id)
#/params?params1=32&params2=43

@app.route("/register")
def register():
    register_user = forms.RegisterUser()
    return render_template('register.html', form=register_user)


@app.route("/newficha")
def newficha():
    new_ficha = forms.FichaPersonaje()
    return render_template('newficha.html', form=new_ficha)

@app.route("/editficha")
def editficha():
    return render_template('editficha.html')

@app.route("/fichas")
def fichas():
    return render_template('fichas.html')

@app.route("/relaciones")
def relaciones():
    return render_template('relaciones.html')

@app.route("/cronologias")
def cronologias():
    return render_template('cronologias.html')

@app.route("/jugadores")
def jugadores():
    return render_template('jugadores.html')

# starting server
if __name__ == '__main__':
    app.run(debug= True, port=9000)