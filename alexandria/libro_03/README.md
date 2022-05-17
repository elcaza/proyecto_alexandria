# Libro 03 - Docker
`@author elcaza - José Antonio Martínez Balderas`

¡Perfecto! Entonces también conoces lo básicos sobre programación en bash.
Nos contaron que también conocias lo básicos de Docker, ¿Crees podernos ayudar a desplegar una configuración básica?

### Requesitos
+ Máquina Debian 10/11 ó Máquina Ubuntu 20.04 LTS

## Objetivo
Poner en práctica las habilidades de:
- Administración de sistemas Linux
- Administración de redes en VMware
- Aplicación de Shell script para la resolución de problemas

## Índice

### Capítulo 1 - Instalación de Docker
Realiza lo siguiente:
1. Realiza la instalación de Docker en una máquina Linux
1. Añade tu usuario al grupo Docker

### Capítulo 2 - Docker File
1. Genera un `Dockerfile` que:
	+ Genere un usuario para correr la aplicación (el usuario debe ser tu numero de cuenta)
	+ Instale Apache
		+ La página mostrada por apache debe tener "Hola, soy $USUARIO"
			+ Donde usuario se sustituye por el número de cuenta
	+ Sentencias a utilizar: `RUN, USER, COPY`
1. Subir su imagen de Docker a Dockerhub
1. Descarga y ejecuta el script `evaluador6.sh` y como argumento el nombre de tu script `instala_docker.sh`
	1. Guarda tu `flag` (Recuerda que se genera y es única para tu usuario)
1. Sube tu Dockerfile y lo necesario para que funcione el docker build a github


En este capítulo podrás realizar:
1. Instalación de Docker
1. Configuración de permisos y usuarios de Docker
1. Configuración de DockerFile
1. Creación y despliegue de instancias de Docker a través de DockerFile

### Capítulo 2 - Configuraciones de red
En este capítulo podrás realizar:
1. Creación de Switch virtuales
1. Asignación de segmentos de red
1. Administración de interfaces de red en VMware
1. Asignación de IPs estáticas
