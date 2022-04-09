## Capitulo 0: Configuración inicial
Sea usted bienvenido ¿Se encuentra listo para trabajar? 
Esperamos que sí porque tenemos mucho por hacer; nos han informado que quizá tú puedas apoyarnos con el despliegue de las siguientes configuraciones.

Por cierto, para completar el capítulo 0 será necesario que se resuelva primero parte del capítulo 1. Sin embargo, haga todo lo que esté en sus manos para resolver la mayor parte de este capítulo.

> Disclaimer: El laboratorio ha sido elaborado para trabajar con VMware Workstation, actualmente ofrece una licencia trial de 30 días. Sin embargo, sientase libre de utilizar cualquier otra plataforma de virtualización siempre y cuando cumpla con las especificaciones de segmentos de red. En caso de elegir otros segmentos y direcciones IP recuerde modificar el archivo /opt/laboratorio_so/settings.conf

## Máquinas requeridas
+ Máquina examen (Descargar, link pendiente)
	+ hostname: examen
+ CentOS Stream 8 (Crear)
	+ Usuario: user_centos
	+ hostname: cs8
+ Ubuntu Server 20.04 LTS (Crear)
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
> En caso de elegir otros segmentos y direcciones IP recuerde modificar el archivo `../settings.conf`

~~~bash
# Máquina examen (Debian)
IP_DEBIAN="172.21.21.100"
IP_DEBIAN2="172.23.23.222"

# Máquina Centos Stream
IP_CENTOS="172.23.23.200"

# Máquina Ubuntu20
IP_UBUNTU="172.21.21.102"
~~~

----------------------------------------------------------------------------------------
# Revisores de examen

## Capítulo 1 - Configuraciones iniciales
Una vez que hayas realizado todos los pasos requeridos por Capítulo 1: Configuraciones iniciales
1. Ejecuta el revisor de exámen
	- Descripciones sujetas a modificación
	- ¡Recuerda guardar el FLAG obtenido!