## Desarrollo de la actividad 2 de la asignatura de CC3S2

1. **Primero preparamos preparamos el entorno de desarrollo esto con la función `prepare` del script.

    * Visualizamos contenido de directorio, el cual muestra solo el script, ademas podemos ver que no tiene permisos de ejecución.

      ![](img/image.png)

    * Damos permisos de ejecución con `chmod +x Respuestas-actividad2.sh`, al listar nuevamente, veremos que el archivo cambia de color y tiene los permisos de ejecución para todos los usuarios (-rwx el x indica que el archivo se puede ejecutar)

      ![](img/image-1.png)

    * Preparamos el entorno de desarrollo con `./Respuestas-actividad2.sh prepare`, esto generara algunas carpetas necesaria, ademas de crear el archivo `miapp/app.py` el cual ya tendrá implementado un servicio web de nuestro app, ademas de generar un entorno virtual de python `.venv`

      ![](img/image-2.png)

    * Ejecutamos la aplicación con `./Respuestas-actividad2.sh run`, esto levantara la aplicación en nuestro local y esta disponible para su acceso.

      ![](img/image-3.png)

    * Lo anterior guardo el log de la ejecución de la aplicación en un archivo dentro de la carpeta `evidencias` la cual mostramos a continuación.

      ![](img/image-4.png)

    * También podemos acceder desde el navegador a dicho servicio web, ya que estamos seguros que el servicio web ya esta ejecutándose,

      ![](img/image-5.png)

    * Generalmente accedemos a una pagina web mediante un dominio, por ejemplo `miapp.local`, como por el momento no lo tenemos configurado, esto nos generara un error.

      ![](img/image-6.png)

    * Añadimos el dominio `miapp.local` para poder ser accedido mediante este, para ello, primero ejecutamos el script con `./Respuestas-actividad2.sh hosts-setup`, esto configurando el dominio a nuestro host.

      ![](img/image-7.png)

    * Ahora que ya tengo mi ip asociado a mi dominio, hacemos un demo con el DNS que se resuelva correctamente.

      ![](img/image-8.png)

    * Configuramos un certificado con el comando `./Respuestas-actividad2.sh tls-cert`, esto generara los certificados en la carpeta `certs`.

      ![](img/image-9.png)

    * Configuramos Nginx.

      ![](img/image-10.png)

    * Con los pasos anteriores ya listos, ahora podemos acceder a la aplicación web mediante el dominio `miapp.local`.

      ![](img/image-11.png)

    * Realizamos alguna pruebas de tls.

      ![](img/image-12.png)

    * Cada paso que se realizo, fueron registrando los logs en la carpeta evidencias.

      ![](img/image-13.png)