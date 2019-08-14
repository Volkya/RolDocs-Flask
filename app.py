from flask import Flask, render_template, session, redirect, url_for, escape, request, make_response, flash
import forms
#from flask_wtf import CSRFProtect
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
    if 'username' in session:
        username = session['username']
        print (username)
    #custome_cookie = request.cookies.get('custome_cookie', 'Undefined')
    #print(custome_cookie)
    return render_template('index.html')


@app.errorhandler(404)
def notfound(e):
    return render_template('404.html'), 404

@app.route("/cookie")
def cookie():
    response = make_response(render_template('cookie.html'))
    response.set_cookie('custome_cookie', 'Eduardo')
    return response


@app.route("/login", methods=['GET', 'POST'])
def login(title='parrafotest'):
    login_form = forms.LoginUser(request.form)

    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        sucess_message = 'Bienvenido {}'.format(username)
        flash(sucess_message)

        session['username'] = login_form.username.data


    return render_template('login.html', title=title, form = login_form)


@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login'))

#http://127.0.0.1:9000/params?params1=Eduardo&params2=Pepe
@app.route("/params/")
@app.route("/params/<user>/<int:id>")
def params(user = "no hay valor", id = "no"):
    params1 = request.args.get('params1', '1 no contiene parametros')
    return "El parametro es: {} {} ".format(user, id)
#/params?params1=32&params2=43

@app.route("/register", methods = ['GET', 'POST'])
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