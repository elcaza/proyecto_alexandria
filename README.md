# Laboratorio de sistemas operativos

## Descripción
Este es un laboratorio diseñado para que, en conjunto con los materiales proporcionados, el estudiante desarrolle sus habilidades en los siguientes temas:
- Administración de máquinas y redes virtuales con VMware
- Administración de Sistemas Operativos Linux
- Desarrollo de scripts de administración a través de bash scripting
- Creación, despligue y uso de tecnologías de contenedores

## Carácteristicas
1. Fácil despligue para el alumno: 
	- Instalas VMware
	- Descargas la máquina examen
	- Creas una máquina CentOS Stream
	- Creas una máquina Ubuntu 
	- Configuras los adaptadores virtuales de red
	- Configuras las direcciones IP de cada una
	- Comienzas los retos (la configuración por sí misma es el primer reto y cuenta con su propio evaluador)
1. Fácil despligue para el evaluador: 
	- Asignas la actividad
	- Creas un Formulario de Google Forms donde se guardarán las respuestas de cada alumno
	- Exportas el formulario de Google Forms
	- Corres el evaluador automático y lees los resultados
1. Gamificación y evaluación automática
	- Se incluyen `evaluadores`, estos son programas que corroborarán que se hayan resuelto los retos de manera correcta
		- Da sugerencias para solucionar retos no completados en caso de que detecte algún error
		- Otorga una FLAG personalizada tras terminar el reto de manera correcta
1. Mecanismos de evaluación con protección contra fraude
	- Los `evaluadores` otrogan flags personalizada con la que un docente podrá corroborar que no hubo trampa alguna
	- A través de un formulario en Google Forms se hará el registro de cada FLAG obtenida por el usuario
	- Tras exportar el documento generado en Google Forms el docente/evaluador podrá correr un script que analizará los resultados obtenidos por cada estudiante y se generará un documento con:
		- Calificación obtenida
		- Posibles casos de fraude (copias de trabajo)
		- Inconsistencias 
1. Material de enseñanza
	- Se incluye material de enseñanza para que el alumno pueda resolver cada reto
- Material resolutivo
	- Se incluyen vídeos resolutivos de cada ejercicio
1. Licencia CC BY y código Open Source
	- Lo puedes utilizar para cualquier fin
	- Puedes añadir nuevos retos y examenes


## Campos de aplicación

### Campo académico
Gracias a su fácil implementación este laboratorio es ideal para acompañar cursos de:
- Sistemas Operativos
- Redes
- Programación

### Sector privado
Gracias a su fácil implementación este laboratorio podría acompañar actividades como
- Competencias al estilo Capture The Flag
- Capacitación de personal en la introducción de administración de Sistemas Operativos
- Examen filtro en el reclutamiento de ciertos perfiles tecnológicos

----------------------------------------------------------------------------------------
# Detalles de las máquinas

## Máquina examen
+ Sistema Operativo: Debian 10
+ Se proporciona mediante el siguiente link (Aquí irá un link)
+ IP: 172.21.21.100, 172.23.23.222
+ Usuarios:
	+ root
	+ elcapitan_bot
	+ e($CUENTA)
	+ e($CUENTA)dos
+ Archivos:
	+ /opt/laboratorio_so/
		+ /opt/laboratorio_so/capitulo_0/
			+ revisor_0.sh
			+ README.md
		+ /opt/laboratorio_so/capitulo_1/
			+ revisor_1.sh
			+ README.md
		+ /opt/laboratorio_so/capitulo_2/
			+ revisor_2.sh
			+ README.md
		+ /opt/laboratorio_so/capitulo_3/
			+ revisor_3.sh
			+ README.md
		+ /opt/laboratorio_so/capitulo_4/
			+ revisor_4.sh
			+ README.md
		+ /opt/laboratorio_so/capitulo_5/
			+ revisor_5.sh
			+ README.md
		+ settings.conf (ips, configuraciones, étc.)
		+ README.md
	
## Máquina CentOS Stream 8
+ Sistema Operativo: CentOS Stream 8
+ Debes crearla
+ IP: 172.23.23.200
+ Usuarios:
	+ root
	+ elcapitan_botc
	+ c($CUENTA)
	+ c($CUENTA)dos

## Máquina Ubuntu 20.04 LTS
+ Sistema Operativo: Ubuntu 20.04 LTS
+ Debes crearla
+ IP: 172.21.21.100
+ Usuarios:
	+ root
	+ elcapitan_botu
	+ u($CUENTA)
	+ u($CUENTA)dos

----------------------------------------------------------------------------------------
# Revisores de examen

## Capítulo 0 - Configuraciones iniciales
Una vez que hayas realizado todos los pasos requeridos por Capítulo 0: Configuraciones iniciales
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!

## Capítulo 1 - Debian
Una vez que hayas realizado todos los pasos requeridos por la máquina (Máquina examen (Debian 10) (172.21.21.100)) 
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!

## Capítulo 2 - CentOS Stream
Una vez que hayas realizado todos los pasos requeridos por la máquina (Máquina CentOS Stream 8 (172.23.23.200) ) 
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!

## Capítulo 3 - Ubuntu
Una vez que hayas realizado todos los pasos requeridos por la máquina (Máquina Ubuntu 20.04 LTS (172.21.21.102) ) 
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!

## Capítulo 4 - Programacion
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!

## Capítulo 5 - Contenedores
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!

----------------------------------------------------------------------------------------
# Descripción de los retos

## Capitulo 0: Configuración inicial
Sea usted bienvenido ¿Se encuentra listo para trabajar? 
Esperamos que sí porque tenemos mucho por hacer; nos han informado que quizá tú puedas apoyarnos con el despliegue de las siguientes configuraciones.

> Disclaimer: El laboratorio ha sido elaborado para trabajar con VMware Workstation, actualmente ofrece una licencia trial de 30 días. Sin embargo, sientase libre de utilizar cualquier otra plataforma de virtualización siempre y cuando cumpla con las especificaciones de segmentos de red. En caso de elegir otros segmentos y direcciones IP recuerde modificar el archivo /opt/laboratorio_so/settings.conf

## Máquinas requeridas
+ Máquina examen (Descargar, link pendiente)
	+ hostname: examen
+ CentOS Stream 8 (Crear)
	+ Usuario: user_centos
	+ hostname: cs8
+ Ubuntu 20.04 LTS (Crear)
	+ Usuario: user_ubuntu
	+ hostname: u20

## Configuraciones de red
1. Crear una nueva interfaz de red en modo NAT **(172.21.21.0)**
	+ Conectar la máquina examen a esta interfaz
	+ Conectar la máquina Ubuntu 20.04 LTS a esta interfaz 
1. Crear una nueva interfaz de red en modo NAT **(172.23.23.0)**
	+ Conectar la máquina examen a esta interfaz
	+ Conectar la máquina CentOS Stream 8 a esta interfaz
1. Asignar una IP fija a cada máquina 
	+ Máquina examen (172.21.21.100, 172.23.23.222)
	+ Máquina CentOS Stream 8 (172.23.23.200) 
	+ Máquina Ubuntu 20.04 LTS (172.21.21.102)
1. Una vez terminadas estas configuraciones ejecute el revisor de examen correspondiente (Revisores de examen)
	+ Debes dirigirte a la sección "Revisores de examen" y seguir las instrucciones del Capítulo 0


## Notación importante
Para futuras referencias 
> En caso de elegir otros segmentos y direcciones IP recuerde modificar el archivo /opt/laboratorio_so/settings.conf

~~~bash
# Máquina examen (Debian)
IP_DEBIAN="172.21.21.100"
IP_DEBIAN2="172.23.23.222"

# Máquina Centos Stream
IP_CENTOS"172.23.23.200"

# Máquina Ubuntu20
IP_UBUNTU="172.21.21.102)"
~~~


## Capítulo 1
¡Vaya, quién lo diría! Para acceder al `revisor_0` es necesario acceder a la máquina examen, pero no tenemos la contraseña; el ex administrador de sistemas se enojó y ¡Nos quitó todo el accesó! Incluso se rumora que estropeo ciertas configuraciones importantes.
No obstante, me han comentado que eres una persona una increíble ¿Puedes resolverlo? 

Por cierto, dados los antecedentes, el jefe ha pedido que implementes algunas cosas; adjunto la lista.

### Máquina examen (Debian 10) (172.21.21.100)
1. Hackea el password de root 
	1. ¿Quieres una pista? Opciones del grub
1. Ahora que tienes acceso, ¿Hay alguien más en el sistema? Corrobora que seas el único usuario loggeado
	1. ¿Requieres ayuda? comando `who` (Tranquilo, es un laboratorio en red NAT, que haya otro usuario loggeado es improbable. De haberlo tienes un serio problema en tu red local o iniciaste sesión dos veces)
1. Al jefe le interesa la carpeta de `/opt/laboratorio_so/` y teme que hayan borrado los archivos ¿Puedes ver que todo este bien? Y si no lo está ¿Puedes solucionarlo?
	1. Si quieres ayuda puedes seguir leyendo, pero no la necesitas ¿O sí?
		1. Ya habrás notado que la carpeta `/opt/laboratorio_so/` ahora está comprimida 
		1. Esta comprimida y ¡Con password! Seguro que el sysadmin anterior lo hizo ¿Habrá quedado en algún historial? Antes de actuar consultas con quienes te han contratado, porque si entras sin autorización previa al directorio `/home/` de otros usuarios podrías estar incurriendo en un delito. Ellos aprueban que lo hagas.
		1. Todo usuario tiene un `.bash_history` en donde quedan registrados todos los comandos realizados por un usuario
			1. Lee el archivo `.bash_history` de admin1 y también investiga
			1. Lee el archivo `.bash_history` de admin2
			1. Ahora tienes un password 
				1. Puedes probar si el password es para el archivo `/opt/laboratorio_so.zip` 
1. ¿Has logrado realizar el reto anterior? Consideraste el aspecto legal, si no lee el punto anterior completo.
1. Instala el páquete de `sudo`, (Para que root no sea el único usuario con privilegios)
	1. ¿No se pudo? ¿Ya sabes cómo repararlo o quieres ayuda?
		1. Sigue leyendo para recibir ayuda, pero anda, esfuerzate ¡Lo sabes!
			1. Bien, ya qué; la pista es: Repara los repositorios para que puedas descargar software
1. Elimina a los usuarios intrusos
	1. Ubica quienes son
	1. Eliminalos del sistema (Borra también su carpeta home)
	1. Asegurate de solamente eliminar a los usuarios intrusos
1. Crea tu propio usuario con la letra "e" y tu número de cuenta, por ejemplo "e311266123" y añadelo al grupo sudo
1. Crea tu propio usuario con la letra "e" y tu número de cuenta y la terminación dos, por ejemplo "e311266123dos" y dale permisos en el archivo `sudoers`
1. Instala mate-desktop
1. Cambia el tipo de inicio para que siempre inicie con intefaz gráfica
1. Instala el siguiente paquete: `paquete.deb`
1. Instala Apache
1. Asegurate de que el servicio e Apache y SSH siempre inicien de manera automática tras el reinicio
1. Haz que a este servidor únicamente te puedas loggear mediante llave SSH
1. Ejecuta el revisor del examen
	+ ¿No ha funcionado? corrige que funcione. La ejecución debe ser tal cual:
	+ `revisor_0.sh`
1. Ejecuta el revisor del examen
	+ ¿No ha funcionado? corrige que funcione. La ejecución debe ser tal cual:
	+ `revisor_1.sh`
1. Si has logrado todos los retos crea un snapshot

## Capítulo 2
¡Bien hecho! Si has llegado hasta aquí es porque tienes conocimientos.
Ahora, el jefe ha pedido un Servidor CentOS Stream 8, debido a su estabilidad. ¿Tú qué sabes del tema?
Como sea, este servidor será sencillo: Un poco de hardening y servicios básicos. 
¿Nos ayudas? Adjuntamos la lista de deberes

### Máquina CentOS Stream 8 (172.23.23.200) 
1. Crea tu propio usuario con la letra "c" y tu número de cuenta, por ejemplo "c311266123" y añadelo al grupo sudo o su equivalente en CentOS
1. Crea tu propio usuario con la letra "c" y tu número de cuenta y la terminación dos, por ejemplo "c311266123dos" y dale permisos en el archivo `sudoers`
1. Crea un usuario llamado `elcapitan_botc` con el password `alamar123##Cs8`
1. Crea tu propia llave SSH, con la opción para añadir un comentario pon tu nombre de usuario
1. Añade tu llave pública al servidor del exámen (Máquina examen)
1. Comprueba que puedes hacer login mediante llave pública
1. Instala Apache, PHP Y SSH
	+ Haz que Apache escuche en el puerto 8080
	+ Haz que tu servidor SSH solamente permita el login mediante llave pública
1. Haz que se muestre la página de información de PHP en la ruta raíz de tu servidor, es decir, deberá aparecer la página de información de tu PHP al visitar
	+ http://localhost:8080/
	+ http://127.0.0.1:8080/
	+ http://$IP_CENTOS:8080/
1. Descarga la llave pública de la "máquina examen" y añadela a tu servidor, con el objetivo de que ahora la máquina examen pueda hacer login en tu servidor con su llave privada. Es decir, el paso 5 pero invertido.
1. Ejecuta el evaluador del Capítulo 2
1. Si has logrado todos los retos crea un snapshot


## Capítulo 3
Excelente, si has llegado hasta este punto significa que has dominado los aspectos básicos de CentOS. Ubuntu está basado en Debian, por lo que en realidad seguramente te será mucho más sencillo.

### Máquina Ubuntu 20.04 LTS (172.21.21.102)
1. Crea tu propio usuario con la letra "u" y tu número de cuenta, por ejemplo "u311266123" y añadelo al grupo sudo
2. Crea tu propio usuario con la letra "u" y tu número de cuenta y la terminación dos, por ejemplo "u311266123dos" y dale permisos en el archivo `sudoers`
3. Crea un usuario llamado `elcapitan_botu` con el password `alamar123##U20`
4. Crea tu propia llave SSH, con la opción para añadir un comentario pon tu nombre de usuario
5. Añade tu llave pública al servidor del exámen (Máquina examen)
6. Comprueba que puedes hacer login mediante llave pública
7. Instala LAMP
8. Instala wordpress en una carpeta llamada `cms` de tal manera que se pueda acceder mediante:
	+ http://localhost/cms
	+ http://127.0.0.1/cms
	+ http://$IP_UBUNTU/cms
9. Asegurate de que el servicio e Apache y SSH siempre inicien de manera automática tras el reinicio
10. Ejecuta el evaluador de la Capítulo 3
11. Si has logrado todos los retos crea un snapshot

## Capítulo 4
¡Felicidades! Has logrado pasar los temas básicos de administración en Linux. El antigüo sysadmin debe estar muy molesto porque te encontramos. Pero... ¿Qué tan bueno eres programando?
Nada tan complicado, un poco de Bash Scripting...
Te adjuntamos los retos.

### Retos de programación

1. Script import_public_key.sh
	1. Crea un script para descargar la llave pública de la "máquina examen" y añadela a tu servidor, con el objetivo de que ahora la máquina examen pueda hacer login en tu servidor con su llave privada. Es decir, el paso 5 pero invertido.
	1. Descarga el primer evaluador de programacion de:
		+ http://$IP_DEBIAN/programacion/evaluador1.sh
	1. Mueve el archivo `evaluador1.sh` a un lado de tu script generado en el paso 1
	1. Ejecuta el script `evaluador1.sh` y como argumento el nombre de tu `script.sh`
	1. Guarda tu `flag` (Recuerda que se genera y es única para tu usuario)

1. Script encuentra_duplicados.sh
	1. Descarga los archivos de:
		+ http://$IP_DEBIAN/programacion/utils/duplicados.tar.gz
	1. Descomprime los archivos descargados
	1. Elabora un script que te dé una lista de los archivos duplicados
	1. Descarga el evaluador2
		+ http://$IP_DEBIAN/programacion/evaluador2.sh
	1. Ejecuta el script `evaluador2.sh` y como argumento el nombre de tu lista de duplicados `lista_duplicados.txt`
	1. Guarda tu `flag` (Recuerda que se genera y es única para tu usuario)

1. Script descarga_ssh.sh
	1. Crea un script que por medio de SSH y llavé pública descargue un el archivo `ruta`
	1. Ejecuta el script `evaluador3.sh` y como argumento el nombre de tu lista de duplicados `lista_duplicados.txt`
	1. Guarda tu `flag` (Recuerda que se genera y es única para tu usuario)

1. Script filtra_correos.sh
	1. Descarga los archivos de:
		+ http://$IP_DEBIAN/programacion/utils/correos.txt
	1. Haz las operaciones necesarias para convertir todos los `.at.` en `@`
	1. Filtra todo lo que sea basura y solamente deja los correos de tal manera que:
		+ Se eliminen los duplicados
		+ Esten ordenados
		+ Ejemplo lista salida:
		```
		aaa@dominiofake.com
		abc@dominiofake.com
		...
		xyz@dominiofake.com
		zzz@dominiofake.com
		```
	1. Ejecuta el script `evaluador4.sh` y como argumento el nombre de tu script `filtra_correos.sh`
	1. Guarda tu `flag` (Recuerda que se genera y es única para tu usuario)

1. Script obten_usuarios.sh
	1. Descarga los archivos de:
		+ http://$IP_DEBIAN/programacion/utils/usuarios.txt
	1. Haz las operaciones necesarias para extraer a todos los usuarios cuya shell sea "/bin/bash"
	1. Haz las operaciones necesarias para que el resultado sea:
		```
		username:/bin/bash
		username:/bin/bash
		username:/bin/bash
		```
	1. Filtra todo lo que sea basura y solamente deja los correos de tal manera que:
		+ Se eliminen los duplicados
		+ Esten ordenados
		+ Ejemplo lista salida:
		```
		username1:/bin/bash
		username2:/bin/bash
		...
		username3:/bin/bash
		username4:/bin/bash
		```
	1. Ejecuta el script `evaluador5.sh` y como argumento el nombre de tu script `obten_usuarios.sh`
	1. Guarda tu `flag` (Recuerda que se genera y es única para tu usuario)

1. Script instala_docker.sh
	1. Desarrolla un script que instale docker de manera automática en un debian 10
	1. Descarga y ejecuta el script `evaluador6.sh` y como argumento el nombre de tu script `instala_docker.sh`
	1. Guarda tu `flag` (Recuerda que se genera y es única para tu usuario)

## Capítulo 5
¡Perfecto! Entonces también conoces lo básicos sobre programación en bash.
Nos contaron que también conocias lo básicos de Docker, ¿Crees podernos ayudar a desplegar una configuración básica?

### Retos de contenedores
** Es requisito que el reto de **Script instala_docker.sh** haya sido completado correctamente

Realiza lo siguiente:
1. Realiza la instalación de Docker en la máquina Ubuntu 20
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
