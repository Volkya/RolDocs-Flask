from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from wtforms.fields.html5 import EmailField


#Funcion para el honeypot


#Registro de usuarios
class RegisterUser(Form):
    username = StringField('Username', [
        validators.DataRequired(message='El username es requerido'),
        validators.Length(min=2, max=25, message='Inserta un dato valido')
    ])
    email = EmailField('Email', [
        validators.DataRequired(message='El mail tambien es necesario!')
    ])
    password = PasswordField('Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repita la contraseña')
    comment = StringField('Comentario', [
        validators.DataRequired(message="El comentario tambien")
    ])
    #honeypot = TextField("", [length_honeypot])

#Conexión de usuarios
class LoginUser(Form):
    email = EmailField('Email', [
        validators.DataRequired(message='No completaste tu user!')
    ])
    password = PasswordField('Contraseña', [
        validators.DataRequired(message="Tu contraseña es requerida")
    ])


#Registro de fichas
class FichaPersonaje(Form):
    pjname = StringField('NOMBRE DEL PERSONAJE', [validators.DataRequired(message="No olvides tu nombre")])
    pb = StringField('Played by', [validators.DataRequired(message="No olvides tu nombre")])
    edad = StringField('EDAD', [validators.DataRequired(message="No olvides tu nombre")])
    raza = StringField('RAZA', [validators.DataRequired(message="No olvides tu nombre")])
    orientacion = StringField('ORIENTACIÓN SEXUAL', [validators.DataRequired(message="No olvides tu nombre")])
    ocupacion = StringField('Ocupación', [validators.DataRequired(message="No olvides tu nombre")])
    nacionalidad = StringField('NACIONALIDAD', [validators.DataRequired(message="No olvides tu nombre")])
    residencia = StringField('Residencia', [validators.DataRequired(message="No olvides tu nombre")])
    grupo = StringField('GRUPO', [validators.DataRequired(message="No olvides tu nombre")])
    psico = TextAreaField('PSICOLOGIA', [validators.optional(), validators.length(max=400)])
    fisico = TextAreaField('FISICO', [validators.DataRequired(message="No olvides tu nombre")])
    historia = TextAreaField('HISTORIA', [validators.DataRequired(message="Sin historia no hay ficha papu")])