#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
hackido - 2020 - por jero98772
hackido - 2020 - by jero98772
"""
from Crypto.Cipher import AES
from Crypto import Random
import base64
import hashlib
def unpad(s):
	return s[:-ord(s[len(s) - 1:])]
def pad(s):
	BLOCK_SIZE = 16
	return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
def enPassowrdHash(password):
	hashPassowrd = hashlib.sha256(password.encode("utf-8")).digest()
	return hashPassowrd
def enPassowrdStr(password):
	hashPassowrd = str(hashlib.sha256(password.encode('utf-8')).digest())
	return hashPassowrd
def enPassowrdHashHex(password):
	hashPassowrd = hashlib.sha256(password.encode("utf-8")).hexdigest()
	return hashPassowrd
def enPassowrdStrHex(password):
	hashPassowrd = str(hashlib.sha256(password.encode('utf-8')).hexdigest())
	return hashPassowrd
def encryptAES(text, password):
	private_key = enPassowrdHash(password)
	text = pad(text)
	iv = Random.new().read(AES.block_size)
	cipher = AES.new(private_key, AES.MODE_CBC, iv)
	return base64.b64encode(iv + cipher.encrypt(text))
def decryptAES(text, password):
	private_key = enPassowrdHash(password)
	text = base64.b64decode(text)
	iv = text[:16]
	cipher = AES.new(private_key, AES.MODE_CBC, iv)
	mensaje =  unpad(cipher.decrypt(text[16:]))
	return mensaje.decode()