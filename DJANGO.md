# Notas de DJANGO
* Utiliza una característica de autenticación
* Un App en Django encapsula funcionalidad
* 


## Comandos
* Instalar Django
  ```bash
  pip install Django
  ```
1° Crear un proyecto de Django
```bash
django-admin startproject <nombre_proyecto> .
```
2° Iniciar un proyecto en Django
```bash
python mange.py runserver
```
3° Crear un super usuario
```bash
python manage.py createsuperuser
```
4° Crear una app
```bash
python manage.py startapp <nombre_app>
```
5° Crear las migraciones
```bash
python manage.py makemigrations <nombre_app>
```

6° Sincronizar migraciones
```bash
python manage.py migrate
```