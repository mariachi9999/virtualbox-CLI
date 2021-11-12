1. Creo una nueva VM.
2. Ir a configuración > Red > Conectado a => Adaptador de puente.
3. Ir a configuración > Almacenamiento > Controlador IDE => Seleccionar ISO SO seleccionado.
4. Iniciar la VM y seguir los pasos de instalación necesarios.
5. Tener cuidado, cuando se pregunta por la opción de aceptar SSH, tildar casilla.

6. Conectar vm con ssh
   Si necesitamos que un servidor Linux se conecte a otro (o a otro dispositivo con SSH) de forma automática - siguiendo un script, por ejemplo - y no queremos que el servidor destino nos pida password en cada conexión, podemos evitarlo usando un par de claves pública/privada, donde dejamos la parte privada de la clave en el servidor origen e insertamos la parte pública en el servidor destino.
   El paquete SSH tiene comandos específicos built-in para facilitarnos esta tarea: ssh-keygen y ssh-copy-id.

En origen
Para crear el par de claves usaremos el comando ssh-keygen en el servidor origen.
Ahora, copiamos la parte pública de la clave hacia el servidor destino con el comando ssh-copy-id.
ssh-copy-id usuario@destino

A partir de este momento, si ejecutamos ssh usuario@destino en origen, podremos conectar a la máquina destino sin tener que introducir el password del usuario con el que nos conectamos.

Consideraciones:
Para Fedora, revisar https://linuxconfig.org/how-to-install-start-and-connect-to-ssh-server-on-fedora-linux
Para Ubuntu, revisar https://linuxize.com/post/how-to-set-up-ssh-keys-on-ubuntu-20-04/
Para no tener que tipear "root@usuario" cada vez que quisieramos acceder a esa vm, podemos configurar un archivo config y renombrar esa conexion; ver https://linuxize.com/post/using-the-ssh-config-file/ .

---

Buena práctica=>no acceder como root, sino mas bien como otro usuario.
Para ello, seguir la siguiente guía:
https://conpilar.es/como-otorgar-privilegios-de-root-a-un-usuario-en-linux/

Consideración Fedora:
usermod -aG <group> <user-name> Para darle permisos admin, en group tipear wheel

---

7. Ya dentro de nuestra VM, podemos a proceder a instalar Docker.
   https://docs.docker.com/engine/install/ubuntu/

8. Una vez instalado Docker, podemos instalar imagenes de aquellos software que necesitemos; por ejmplo jenkins.
   Para eso, podemos acceder a dockerhub.
