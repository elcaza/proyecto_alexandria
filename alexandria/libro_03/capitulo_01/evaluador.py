#!/usr/bin/python3
# usage: ./evaluador.py
# Evaluador libro_03 capitulo_01

######################################################
# Dependencias
from shutil import which
from os import popen
import os.path
import hashlib
import base64
import codecs

delimitador = "*#*"

######################################################
# Create flag

def create_flag(puntaje):
	actual_script = (os.path.basename(__file__)).strip() + delimitador
	hash_evaluador = (popen("md5sum "+os.path.basename(__file__)).read().split()[0]).strip() + delimitador
	score = str(puntaje).strip() + delimitador
	username = (popen("id -un").read().strip()) + delimitador
	
	flag = actual_script + hash_evaluador + score + username + get_date()
	flag = codecs.encode(flag, "rot_13")
	
	flag_b64 = base64.b64encode(bytes(flag, 'utf-8'))
	flag_b64 = flag_b64.decode('ascii')
	flag_b64 = codecs.encode(flag_b64, "rot_13")
	
	return flag_b64

def get_date():
	return popen("date").read()

######################################################
# Funciones básicas de evaluadores
# Primera parte
def check_docker():
	return check_program("docker")

# Segunda parte
def check_docker_user():
	# Obtiene grupo Docker
	user_docker = popen("cat /etc/group | grep docker").read()
	usuario_actual = popen("echo $USER").read()

	if usuario_actual in user_docker:
		return True
	return False

######################################################
# Funciones adicionales

# Funcion para checar si el programa existe
# True si existe
# False si no existe
def check_program(program):
	return which(program) is not None

######################################################
# Main
def main():
	puntaje = 0

	# Parte 1
	if check_docker():
		puntaje = puntaje+1
	else:
		print("Parece que no tienes instalado Docker")

	# Parte 2
	if check_docker_user():
		puntaje = puntaje+1
	else:
		print("Parece que tu usuario no está autorizado para correr Docker sin _sudo_")

	# Genera Flag
	print("La flag es:\n")
	print(create_flag(puntaje))

if __name__ == "__main__":
	main()