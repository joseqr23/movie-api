# Pasos para deploy

## 1. Instalamos dependencias

```bash
pip install gunicorn
pip install django-environ
```

## 2. Creamos nuestro requirements

```bash
pip freeze > requirements.txt
```
## 3. Creamos nuestro archivo procfile y le añadimos esto
```bash
web: python manage.py migrate && gunicorn movies.wsgi
```
## 4. Creanis nuestra db en railway
Usamos mysql por defecto
[Railway](https://railway.com)

## 5. Configurar las variables de entorno

```python
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```
