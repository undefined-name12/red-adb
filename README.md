<h1 align="center">
<img src="https://image.flaticon.com/icons/png/512/160/160138.png" width="150px"><br>
adb: una herramienta de explotación para dispositivos Android.
</h1>
<p align="center">
Una herramienta que permite buscar dispositivos Android vulnerables en todo el mundo y explotarlos.
</p>

<p align="center">
<a href="https://deno.land" target="_blank">
<img src="https://img.shields.io/badge/Version-1.0.0-7DCDE3?style=for-the-badge" alt="Version">
</p>

#Características
```
Características:
- Módulos de post-explotación para controlar y manipular el dispositivo al que estás conectado. - Escáneres para buscar dispositivos Android vulnerables en todo el mundo y explotarlos.
- Opciones para administrar la cantidad de dispositivos conectados.
- Opciones para verificar si los dispositivos a los que está conectado están conectados o no.
- Búsqueda de IP para obtener información sobre una IP específica.
- Opciones para obtener las direcciones IP de los dispositivos Android vulnerables. [Esto te facilita la vida para que no tengas que buscarla tú mismo]
```

# Obtener las claves API necesarias
Crea una cuenta en censys.io y accede a tu página de cuenta para obtener tu ID de API y tu clave secreta de API gratuitas. Abre 'adbnet.py' y edita tu ID y clave de API aquí:

![image](https://user-images.githubusercontent.com/86132648/124665489-c6588b00-de7a-11eb-984b-b9e3118aba81.png)

Crea una cuenta en shodan.io y accede a tu cuenta para obtener tu clave API gratuita. Una vez copiada, abre 'adbnet.py' y edita tu clave API. Aquí:
![imagen](https://user-images.githubusercontent.com/86132648/124665543-d7090100-de7a-11eb-9ef6-e400227a1359.png)

# Tutorial sencillo
```
Primero, ejecuta el comando 'dump shodan' o 'dump censy' (se recomienda 'dump shodan') para volcar las direcciones IP de los dispositivos vulnerables.

Después de encontrar la dirección IP que quieras probar, ejecuta el comando 'connect' y se te pedirá que ingreses la dirección IP de destino. Una vez que la ingreses, se te pedirá que ingreses el puerto. Puedes intentar ingresar '5555' o '4444', ya que son los puertos más comunes. Si lo deseas, puedes intentar encontrar el puerto específico tú mismo, pero podría llevar algo de tiempo.

Ahora AdbNet intentará conectarse al dispositivo Android vulnerable.
Si no logra conectarse, prueba con otra IP.

Si logras conectarte a un dispositivo, puedes comprobar si realmente estás conectado con el comando "devices".

<¡Advertencia!> ¡Solo puedes conectarte a un dispositivo a la vez! Para cerrar las sesiones, usa el comando "killall". <¡Advertencia!>

Para abrir una shell y ejecutar comandos en el dispositivo, usa el comando "terminal".

Para ejecutar módulos de postexplotación, ejecuta el comando "post" para que se cargue el menú de postexplotación. Después, puedes ejecutar cualquier módulo que desees.

RECUERDA: SI QUIERES CONECTARTE A OTRO DISPOSITIVO, EJECUTA EL COMANDO "killall" Y REPITE EL PROCESO. ```

# Instalación/Cómo ejecutar
```
sudo apt install pq
sudo apt install adb
pip3 install colorama
pip3 install requests
python3 adbnet.py o python adbnet.py o py adbnet.py

CONSEJO: Para quienes son nuevos en esto, si tienen problemas para instalar un módulo de Python, simplemente hagan lo siguiente: pip3 install <modulename>
# Capturas de pantalla
![imagen](https://user-images.githubusercontent.com/86132648/124667060-e2f5c280-de7c-11eb-8f69-2443aa7a7bd3.png)
![imagen](https://user-images.githubusercontent.com/86132648/124667104-f30da200-de7c-11eb-9da3-098fa211a910.png)
