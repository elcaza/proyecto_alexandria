# Capítulo 3
¡Bien hecho! Si has llegado hasta aquí es porque tienes conocimientos.
Ahora, el jefe ha pedido un Servidor CentOS Stream 8, debido a su estabilidad. ¿Tú qué sabes del tema?
Como sea, este servidor será sencillo: Un poco de hardening y servicios básicos. 
¿Nos ayudas? Adjuntamos la lista de deberes

## Máquina CentOS Stream 8 (172.23.23.200) 
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

Editar
# Política sobre la generación de usuarios
Seguir esta política es importante porque de esta manera el evaluador de la práctica analizará ciertos incisos requeridos por la práctica.

## Usuario primario
1. Crea tu propio usuario con la letra "e" y tu número de cuenta, por ejemplo "e311266123" y añadelo al grupo sudo

## Usuario secundario
1. Crea tu propio usuario con la letra "e" y tu número de cuenta y la terminación dos, por ejemplo "e311266123dos" y dale permisos en el archivo `sudoers`
