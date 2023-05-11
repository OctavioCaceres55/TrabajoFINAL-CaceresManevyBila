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
+ Ya creado el superuser, e ingresado ya en panel del administrador, podrás manejar absolutamente todos los datos que fueron cargados. Jugadores, Clubes y Entrenadores. Podrás verificar si todo está correcto, si la información es veridica o, en el caso de haber algún descenso o ascenso, poder actualizarlo. 



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
+ Ya dentro, podrás navegar en 3 diferentes sitios: Clubes, Jugadores y Entrenadores. Cada uno contiene un título, junto con un buscador donde podrás: 
- Filtrar equipos segun su categoria
- Hallar entrenadores 
- Hallar jugadores
+ Luego, podrás leer sobre los mejores entrenadores, en la sección Biogragría. 






```
