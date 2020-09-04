#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
hackido - 2020 - por jero98772
hackido - 2020 - by jero98772
"""
import sqlite3
class dbInteracion():
	def __init__(self,dbName):
		self.dbName = str(dbName)
	def connect(self,tableName):
		self.tableName = str(tableName)
		self.connecting = sqlite3.connect(self.dbName)
		self.cursor = self.connecting.cursor()
		return self.cursor
	def userAvailable(self,user,item):
		self.user = str(user)
		self.item = str(item)
		self.cursor.execute(" SELECT {0} FROM {1}".format(self.item,self.tableName))
		self.users = self.cursor.fetchall()
		for i in range(len(self.users)):
			if self.user in self.users[i]:
				return False
			else:
				return True 
	def saveUser(self,user,password,email,birthday):
		self.user = str(user)
		self.email = str(email)
		self.password = str(password)
		self.birthday = str(birthday)
		self.insertUser = "INSERT INTO {0}(username, email, password, birthday) VALUES( ?, ?, ?, ? );".format(self.tableName)
		self.cursor.execute(self.insertUser,(self.user,self.email,self.password,self.birthday))
		self.cursor.connection.commit()
	def createUser(self):
		self.tableUserFeels = 'CREATE TABLE "{0}Sentimientos" (sentimiento1 TEXT, sentimiento2 TEXT ,sentimiento3 TEXT, sentimiento4 TEXT, sentimiento5 TEXT, sentimiento6 TEXT, val1 INTEGER , val2 INTEGER , val3 INTEGER , val4 INTEGER , val5 INTEGER, val6 INTEGER);'.format(self.user)
		self.tableUserFeelsRnd = 'CREATE TABLE "{0}Sentimientosrnd" (rndsentimiento1 TEXT, rndsentimiento2 TEXT ,rndsentimiento3 TEXT, rndsentimiento4 TEXT, rndsentimiento5 TEXT, rndsentimiento6 TEXT, val1rnd INTEGER , val2rnd INTEGER , val3rnd INTEGER , val4rnd INTEGER , val5rnd INTEGER, val6rnd INTEGER);'.format(self.user)
		self.tableUserOthers = 'CREATE TABLE "{0}Otros" (insultobool INTEGER ,cantidadpersonasinsulto INTEGER  ,quepaso TEXT, insultadobool INTEGER , cantidadpersonasinsultado INTEGER , porque TEXT , quepersonas TEXT ); '.format(self.user)
		self.cursor.execute(self.tableUserFeels)
		self.cursor.connection.commit()
		self.cursor.execute(self.tableUserFeelsRnd)
		self.cursor.connection.commit()
		self.cursor.execute(self.tableUserExp)
		self.cursor.connection.commit()
		self.cursor.execute(self.tableUserOthers)
		self.cursor.connection.commit()
	def findUser(self,user):
		self.user = str(user)
		self.userTuple = (self.user,)
		self.dbcomand =  "SELECT username FROM user Where username =  ? "
		self.cursor.execute(self.dbcomand,self.userTuple)
		self.userHash = self.cursor.fetchall()
		if self.userHash[0] == self.userTuple :
			return True
		else :
			return False
	def findPassword(self,password):
		self.password = str(password)
		self.passwordTulple = (self.password,)
		self.dbcomand =  "SELECT password FROM user Where password =  ? "
		self.cursor.execute(self.dbcomand,self.passwordTulple)
		self.passwordHash = self.cursor.fetchall()
		if  self.passwordHash[0] == self.passwordTulple:
			return True
		else :
			return False
	def closeDB(self):
		self.cursor.close()
		