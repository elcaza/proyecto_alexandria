----------------------------------------------------------------------------------------
# Solución de los retos

## Capitulo 0: Configuración inicial

1. Descargar y crear las máquinas requeridas
1. Crear redes
    - vmnet3 => modo NAT **(172.21.21.0)** con mascara de **(255.255.255.	0)**
    - vmnet4 => modo NAT **(172.23.23.0)** con mascara de **(255.255.255.	0)**
        - En caso de cambiar las IPs de alguna de estas dos redes editar `/opt/settings.conf`
1. Conectar cada máquina a su red y establecer las IPs correspondientes
    - En caso de elegir otros segmentos y direcciones IP recuerde modificar el archivo `/opt/retos/settings.conf`
~~~bash
# Máquina examen (Debian)
IP_DEBIAN="172.21.21.100"
IP_DEBIAN2="172.23.23.222"

# Máquina Centos Stream
IP_CENTOS="172.23.23.200"

# Máquina Ubuntu20
IP_UBUNTU="172.21.21.102"
~~~
1. Resuelve el capítulo 1