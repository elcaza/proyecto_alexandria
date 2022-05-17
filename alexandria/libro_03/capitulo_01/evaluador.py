#!/usr/bin/python3
# usage: ./evaluador.py
# Evaluador libro_03 capitulo_01

######################################################
# Dependencias
from shutil import which
from os import popen
import os.path
import hashlib

######################################################
# Variables globales

# Documento evaluador
evaluador = "evaluador.py"
# Path del documento
path = "/opt/alexandria"

######################################################
# Funciones básicas de evaluadores

# Evaluar la integridad del script
def check_integrity():
	hash_repo = "aaa"
	hash = popen("md5sum "+evaluador).read()
	print(hash)
	print(hash_repo)

	if hash == hash_repo:
		return 1
	return 0

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

	# Evaluar la integridad del script
	if check_integrity == 1:
		puntaje = puntaje+1
		print(puntaje)
	else:
		print("La integridad del script parece corrupta, recuerda que no debes modificarlo")
	
	# Parte 1
	if check_docker():
		puntaje = puntaje+1
		print(puntaje)
	else:
		print("Parece que no tienes instalado Docker")

	# Parte 2
	if check_docker_user():
		puntaje = puntaje+1
		print(puntaje)
	else:
		print("Parece que tu usuario no está autorizado para correr Docker sin _sudo_")

if __name__ == "__main__":
	main()
