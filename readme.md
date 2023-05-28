# Proyecto BaloncestoBlog
## Este proyecto tiene como fin darle al usuario la posibilidad de cargar y buscar a sus jugadores de baloncesto preferidos , junto a clubes y entrenadores más reconocidos del país y del mundo.


## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre, con un nombre representativo
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```

## Instrucciones para entrar al panel administrativo de Django
+ En consola, crear un superuser:
```
python manage.py createsuperuser
```
+ Acceder con user y password via:
```
127.0.0.1:8000/admin
```
+ Ya creado el superuser, e ingresado ya en panel del administrador, podrás manejar absolutamente todos los datos que fueron cargados. Jugadores, Clubes, Artículos, y Entrenadores. Podrás verificar si todo está correcto, si la información es veridica o, en el caso de haber algún descenso o ascenso, poder actualizarlo. 



## Instruccions para navegar en el sitio WEB 
+ Activa el ambiente virutal
+ Ubicate con el comando cd en la carpeta contenedora "BlogBaloncesto"
+ Pon a correr el servidor para iniciar el sitio; corriendo el siguiente comando:
```
python manage.py runserver
```
+ Ingresa, clickeando la direccion subrayada de numeros manteniendo presionado la tecla ctrl:
```
127.0.0.1:8000
```
Aqui accederás a un sitio donde se te dispondrán dos opciones principales: Ir a la sección artículos o ingresar a la base de datos. Previo a ello, te sugerimos crear un usuario o ingresar con el mismo si fue creado con antelacion. 

Si escoges ir a la sección de Artículos, haz click en el botón rojo de Artículos. 
Este te llevará a un nuevo sitio web donde podrás leer artículos exclusivamente relacionados a la pelota naranja y al desarrollo de su juego. Podrás crear tus propios artículos y leer bibliografía escrita por otros. 

Por otro lado, si decides ir a la Base de datos, haz click en el botón azúl que lee "Base de datos" y escoge la categoria en la que deseas hondar: Clubes, Jugadores, Entrenadores. 
En cada una de ellas, podrás ver información sobre perfiles que fueron creados por otras personas y conocerlos.

Esta propuesta fue hecha con el fin de expandir las redes de contactos de los entusiastas del deporte y para los que quieren conocer más sobre las estrellas.






```
