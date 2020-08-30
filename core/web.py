#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
hackido - 2020 - por jero98772
hackido - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from .webUtils import mismaContraseña , minCaracteresPass , contraseñaSegura , camposVacios , enPassowrd , esCorreo
from .dbInteracion import dbInteracion 
app = Flask(__name__)
class webpage():
	@app.route("/")
	def index():
		return render_template("index.html")
	@app.route("/preregistro.html")
	def preregistro():
		return render_template("preregistro.html")
#=========== los que incluyan methods=['GET','POST'] ===========#
#===los que incluyan methods=['GET','POST'] y algo de codigo ===#
	@app.route("/registrarse.html",methods=['GET','POST'])
	def registrarse():
		mensajeErr = ""
		database = "core/dataBases/hackido"
		tableName = "user"
		registroOk = "su registro se completo exitosamente"
		problemaUsuario = "Error 1 el usuario/email ya fue o fueron registrados , puede que ya estes registrado o vuelve a intentar con otro"
		problemaPassword = "Error 2 la contraseña que ingreso no es segura por favor prube una con simbolos letras y nuemros y que tenga minimo 6 caracteres y que concidan/sean iguales "
		problemaVacio = "Error 3 no te puedes registrar si los campos requeridos estan vacios"
		if request.method == 'POST':
			userName = str(request.form["userName"])
			password1 = str(request.form["password"])
			password2 = str(request.form["validacionPassword"])
			diaNacimiento = str(request.form["diaNacimiento"])
			email = str(request.form["email"])
			db = dbInteracion(database)
			db.connect(tableName)
			if db.userAvailable(userName,"username") and db.userAvailable(email,"email") and esCorreo(email):
				if mismaContraseña(password1,password2) and minCaracteresPass(password1,6) and minCaracteresPass(password2,6) and contraseñaSegura(password1) and contraseñaSegura(password2):
					mensajeErr = registroOk
					HashPassowrd = enPassowrd(password1)
					db.saveUser(userName,HashPassowrd,email,diaNacimiento)
					db.createUser()
				else:
					mensajeErr = problemaPassword
			else:
				mensajeErr = problemaUsuario
			if camposVacios(userName,password1,password2,email,diaNacimiento):
				mensajeErr = problemaVacio
			db.closeDB()
		return render_template("registrarse.html",mensaje = mensajeErr)
	@app.route("/login.html")
	def login():
		return render_template("login.html")