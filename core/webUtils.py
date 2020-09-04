#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
hackido - 2020 - por jero98772
hackido - 2020 - by jero98772
"""
import datetime
def mismaContraseña(password1,password2):
	if password1 == password2:
		return True
	else:
		return False
def minCaracteresPass(password,cantidad):
	if len(password) > cantidad:
		return True
	else:
		return False
def contraseñaSegura(password):
	haynumeros = False
	hayletras = False
	haysimbolos = False
	numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	for i in password:
		try:
			if i in numeros:
				haynumeros = True
			elif i in letras:
				hayletras = True
			else:
				if type(int(i)) == type(0):
					haynumeros = True
				elif type(str(i)) == type(""):
					hayletras = True				
		except:
			haysimbolos = True
	if haysimbolos and hayletras and haynumeros:
		return True
	else:
		return False
def camposVacios(userName,password1,password2,email,date):
	if userName == "" and password1 == "" and password2 == "" and email == "" and date == "":
		return False
	else:
		return True
def campoVacio(text):
	if text == "":
		return True
	else: 
		return False
def esCorreo(email):
	if "@" in email and "." in email:
		return True
	else:
		return False
def generatePassword():
	genPassowrd = ""
	for i in range(0,16):
		if len(genPassowrd) >= 16 and len(genPassowrd)-len(hexStr) <= 16:
			num = rnd.randint(0,9999)
			if 32 > num >126:
				char = chr(num)
				genPassowrd += char
			else:
				hexStr = str(hex(hexStr))
				genPassowrd += hexStr
		else:
			break
	return genPassowrd
def testing(item):
	print("\n",5*"---",str(item),"---"*5,"\n")
def fechaStr2Arr(fecha):
	fechaArr = []
	tmp = ""
	for i in str(fecha):
		if i == "-":
			fechaArr.append(tmp)
			tmp = ""
		else :
			tmp += i
	else: 
		fechaArr.append(tmp)
	return fechaArr
def hay29feb(año):
	if año % 4 == 0:
		feb29Booll  = True
	else :
		feb29Booll  = False
	return feb29Booll
def dias29feb(años):
	diasX29feb = años // 4
	return  diasX29feb 
def diasXmes(mes):
	esMesesCon31dias = [True,False,True,False,True,False,True,True,False,True,False,True]
	dias = 0
	for i,j in zip(esMesesCon31dias,range(len(esMesesCon31dias))):
		if i:
			dias += 31
		elif j == 1:
			dias += 28
		else:
			dias += 30
	return dias
def hoyArr():
	hoy = fechaStr2Arr(str(datetime.datetime.today().strftime('%Y-%m-%d')))
def hoyStr():
	hoy = str(datetime.datetime.today().strftime('%Y-%m-%d'))
def diasTotales(dia):
	dia = fechaStr2Arr(dia)	
	años = int(dia[0])
	añosTotales = años * 365
	meses = int(dia[1])
	dias = int(dia[2])
	diasDeMeses = diasXmes(meses)
	if años == 0:
		diasTotales =  diasDeMeses + dias
	else:	
		dias += dias29feb(años)
		diasTotales = añosTotales + dias + diasDeMeses 
	return diasTotales
def diferneciaFecha(antigua,nueva):
	diasAntigua = diasTotales(antigua)
	diasNueva = diasTotales(nueva)
	if diasNueva > diasAntigua:
		difernecia = diasNueva - diasAntigua 
	else:
		difernecia = diasAntigua - diasNueva
	return difernecia