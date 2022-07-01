# Capítulo 2 - DockerFile

## Introducción
¡Excelente! Ahora que tenemos Docker instalado podemos generar un archivo `Dockerfile` para levantar un pequeño servidor web.

## Objetivo
1. Aprender sobre la configuración y despliegue de Docker a través del archivo `DockerFile`
1. Aprender sobre el despliegue de un archivo `DockerFile` a través de github

## Instrucciones
### Capítulo 2 - DockerFile
1. Genera un `Dockerfile` que:
	+ Genere un usuario para correr la aplicación (el usuario debe ser tu numero de cuenta)
	+ Instale Apache
		+ La página mostrada por apache debe tener "Hola, soy $USUARIO"
			+ Donde usuario se sustituye por el número de cuenta
	+ Sentencias a utilizar: `RUN, USER, COPY`
1. Subirlo a Github en conjunto a todo lo necesario para su desplegue (Por ejemplo: La carpeta que usará en caso de usar `COPY`)
1. Crear un archivo con la URL del repositorio

# Revisores de examen

## Capítulo 2 - DockerFile
Una vez que hayas realizado todos los pasos requeridos por el capítulo
1. Ejecuta el revisor de exámen
	- ¡Recuerda guardar el FLAG obtenido!
