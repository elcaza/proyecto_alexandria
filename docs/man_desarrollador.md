# Manual del desarrollador
## Conceptos básicos
Este proyecto es una biblioteca de conocimiento didáctico
Al ser una biblioteca tú puedes:
- Crear tu propio libro
    - Añadir lecciones (capítulos)

## Colaboración

Para colaborar únicamente requieres crear un libro con la siguiente estructura y requisitos:

`/opt/retos/` (Carpeta raíz de instalación)
- libro_01 (carpeta)
    - capitulo_01 (carpeta)
        - `README.md` (Archivo)
            - Descripción de los retos para el capítulo e instrucciones
        - `solucion.md` (Archivo)
            - Solución del capítulo (opcional)
        - `evaluador.sh` (Archivo)
            - Script que evalue de manera automatizada el ejercicio propuesto y asigne una calificación
    - capitulo_02 (carpeta)
        - (Misma estructura que la del _capitulo_01_ y se repite para los capítulos necesarios)
    - evaluador_bot (carpeta)
        - `README.md`
    - `README.md` (Archivo)
        - Describe los objetivos de los capítulos
    - `settings.conf` (Archivo)
        - Configuraciones requeridas por los evaluadores
