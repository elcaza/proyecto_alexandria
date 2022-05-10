# Capítulo 1 - Accediendo al sistema

¡Bienvenido nueva persona encargada de los sistemas!

El sysadmin anterior se enojó con la empresa y extropeó las configuraciones de nuestro servidor. ¡Ahora ya no tenemos acceso!

¿Podrías ayudarnos a solucionar estos problemas?

También, dados los antecedentes, el jefe ha pedido que implementes algunas cosas; adjunto la lista.

## Máquina Alexandria (Debian 10) 

### Primera parte - Accediendo al sistema
1. Hackea el password de root 
	1. ¿Quieres una pista? Opciones del grub
1. Ahora que tienes acceso, ¿Hay alguien más en el sistema? Corrobora que seas el único usuario loggeado
	1. ¿Requieres ayuda? comando `who` (Tranquilo, es un laboratorio en red NAT, que haya otro usuario loggeado es improbable. De haberlo tienes un serio problema en tu red local o iniciaste sesión dos veces)

### Segunda parte - Verificando archivos
1. Al jefe le interesa la carpeta de `/opt/alexandria/` y teme que hayan borrado los archivos ¿Puedes ver que todo este bien? Y si no lo está ¿Puedes solucionarlo?
	1. Si quieres ayuda puedes seguir leyendo, pero no la necesitas ¿O sí?
		1. Ya habrás notado que la carpeta `/opt/alexandria/` ahora está comprimida 
		1. Esta comprimida y ¡Con password! Seguro que el sysadmin anterior lo hizo ¿Habrá quedado en algún historial? Antes de actuar consultas con quienes te han contratado, porque si entras sin autorización previa al directorio `/home/` de otros usuarios podrías estar incurriendo en un delito. Para fines prácticos, lo consultas y ellos aprueban que lo hagas porque tienen un respaldo legal.
		1. Todo usuario tiene un `.bash_history` en donde quedan registrados todos los comandos realizados por un usuario
			1. Lee el archivo `.bash_history` de admin1 y también investiga
			1. Lee el archivo `.bash_history` de admin2
			1. Ahora tienes un password 
				1. Puedes probar si el password es para el archivo `/opt/alexandria.zip` 
1. ¿Has logrado realizar el reto anterior? Consideraste el aspecto legal, si no lee el punto anterior completo.

### Tercera parte - Instalando paquetes
1. Instala el páquete de `sudo`, (Para que root no sea el único usuario con privilegios)
	1. ¿No se pudo? ¿Ya sabes cómo repararlo o quieres ayuda?
		1. Sigue leyendo para recibir ayuda, pero anda, esfuerzate ¡Lo sabes!
			1. Bien, ya qué; la pista es: Repara los repositorios para que puedas descargar software

### Cuarta parte - Administrando los usuarios del sistema
1. Elimina a los usuarios intrusos
	1. Ubica cuáles son
	1. Eliminalos del sistema (Borra también su carpeta home)
	1. Asegurate de solamente eliminar a los usuarios intrusos
1. Crea tu propio usuario primario (ver Política sobre la generación de usuarios) y añadelo al grupo sudo. 
	- Usa el comando `useradd` para crear el usuario
1. Crea tu propio usuario secundario (ver Política sobre la generación de usuarios)" y dale permisos en el archivo `sudoers`
	- Usa el comando `useradd` para crear el usuario
1. Ambos usuarios deben tener su carpeta en `/home` con sus respectivos permisos y dueño

### Quinta parte - Instalando paquetes
1. Instala `vim`, `git`, `openssh-server`

### Sexta parte - Instalando y configurando inicio con interfaz gráfica
1. Instala mate-desktop
1. Cambia el tipo de inicio para que siempre inicie con intefaz gráfica

### Septima parte - Instalando paquetes y habilitando servicios
1. Instala el siguiente paquete: `paquete.deb`
1. Asegurate de que el servicio e Apache y SSH siempre inicien de manera automática tras el reinicio
1. Haz que a este servidor únicamente te puedas loggear mediante llave SSH

# Revisores de examen

## Capítulo 1 - Debian
Una vez que hayas realizado todos los pasos requeridos por la máquina Máquina alexandria (Debian 10) 
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!

# Política sobre la generación de usuarios
Seguir esta política es importante porque de esta manera el evaluador de la práctica analizará ciertos incisos requeridos por la práctica.

## Usuario primario
1. Crea tu propio usuario con la letra "e" y tu número de cuenta, por ejemplo "e311266123" y añadelo al grupo sudo

## Usuario secundario
1. Crea tu propio usuario con la letra "e" y tu número de cuenta y la terminación dos, por ejemplo "e311266123dos" y dale permisos en el archivo `sudoers`
