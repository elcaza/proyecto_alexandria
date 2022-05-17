#!/usr/bin/python3
# usage: ./evaluador.py

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
def check_host():
	print("Hostname")
	host = popen("hostname").read()
	print(host)
	if host == "alexandria":
		print("valido")
		return 1
	print("no")
	return 0

# Segunda parte
def check_path():
	is_dir = os.path.isdir(path)
	if is_dir == True:
		print("exito")
	print(is_dir)

# Tercera parte
def check_programs_3():
	sudo = check_program("sudo")
	if sudo == True:
		print("Correcto")
	print("False")

# Cuarta parte


# Quinta parte
def check_programs_5():
	vim = check_program("vim")
	git = check_program("git")
	ssh = check_program("openssh-server")

	if vim == True:
		print("Correcto")
	print("False")

# Sexta parte
def check_gtarget():
	xorg = check_program("xorg")
	mate = check_program("mate-desktop-environment")
	gdm3 = check_program("gdm3")
	lightdm = check_program("lightdm")
	target = popen("systemctl get-default").read().strip()
	
	if target == "graphical.target":
		print("cumple")
	else:
		print("no")
	print("target")

	print(target)


# Septima parte
def check_system_configs():
	vscode = check_program("code")
	apache = check_program("apache2")
	no_pass =  popen("cat /etc/ssh/sshd_config | grep 'PasswordAuthentication'").read()
	yes_key =  popen("cat /etc/ssh/sshd_config | grep 'PubkeyAuthentication'").read()
	ssh_enable = popen("systemctl is-enabled apache2").read()
	apache_enable = popen("systemctl is-enabled sshd").read()


######################################################
# Funciones adicionales

# Funcion para checar si el programa existe
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
	if check_host() == 1:
		puntaje = puntaje+1
		print(puntaje)
	else:
		print("Parece que no estás ejecutando el script en la máquina alexandria")
	
	# Parte 2
	# check_path()
	check_gtarget()
	pass

if __name__ == "__main__":
	main()
