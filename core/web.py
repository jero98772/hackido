#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
hackido - 2020 - por jero98772
hackido - 2020 - by jero98772
"""
from flask import Flask, render_template, request, flash, redirect ,session
from .webUtils import mismaContraseña , minCaracteresPass , contraseñaSegura , camposVacios , esCorreo , generatePassword,testing
from .dbInteracion import dbInteracion
from .cryptotools import enPassowrdStrHex , enPassowrdHashHex ,enPassowrdStr , enPassowrdHash ,encryptAES ,decryptAES
app = Flask(__name__)
app.secret_key =  str(enPassowrdHash(generatePassword()))
class webpage():
	@app.route("/")
	def index():
		return render_template("index.html")
	@app.route("/preregistro.html")
	def preregistro():
		return render_template("preregistro.html")
	@app.route("/donacionbtc.html")
	def donacionBtc():
		return render_template("donacionbtc.html")
#===los que incluyan methods=['GET','POST'] y algo de codigo ===#
#======================= aplicaion web =========================#
	@app.route("/informar.html" , methods=['GET','POST'])
	def informar():
		if not session.get('loged'):
			return render_template("/login.html")
		else:
			return render_template("/informar.html")
#========================== Registro ===========================#
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
					HashPassowrd = enPassowrdStrHex(password1)
					userNameHash = enPassowrdStrHex(userName)
					diaNacimientoHash = enPassowrdStrHex(diaNacimiento)
					db.saveUser(userNameHash,HashPassowrd,email,diaNacimientoHash)
					db.createUser()
					return redirect("/login.html")
				else:
					mensajeErr = problemaPassword
			else:
				mensajeErr = problemaUsuario
			if camposVacios(userName,password1,password2,email,diaNacimiento):
				mensajeErr = ""
			db.closeDB()
		return render_template("registrarse.html",mensaje = mensajeErr)
	@app.route("/login.html",methods=['GET','POST'])
	def login():
		mensajeErr = ""
		database = "core/dataBases/hackido"
		tableName = "user"
		registroOk = "su registro se completo exitosamente"	
		problemaPassword = "Error 4 la contraseña o el nombre de usuario que ingreso no es valida vuelve a intentar"
		problemaVacio = "Error 3 no te puedes registrar si los campos requeridos estan vacios"
		if request.method == 'POST':
			userName = str(request.form["userName"])
			password = str(request.form["password"])
			db = dbInteracion(database)
			db.connect(tableName)
			if db.findUser(enPassowrdStrHex(userName)) and db.findPassword(enPassowrdStrHex(password)): 
				db.closeDB()
				session['loged'] = True
				session['user'] = userName
				return redirect("/informar.html")
			else:
				print(userName,password)
				print(enPassowrdStrHex(userName),enPassowrdStrHex(password))
				mensajeErr = problemaPassword
				flash(mensajeErr)
				print(mensajeErr)
			db.closeDB()
		return webpage.informar()
