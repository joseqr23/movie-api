# Pasos para deploy

## 1. Instalamos dependencias

```bash
pip install gunicorn
pip install django-environ
pip install mysqlclient
pip install whitenoise
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
MYSQLDATABASE=
MYSQLUSER=
MYSQLPASSWORD=
MYSQLHOST=
MYSQLPORT=
```
## 6. Configurar dominio
Para que el proyecto pueda ser accedido desde un dominio.
Debemos configurar el dominio en railway y en nuestro proyecto.
```python
ALLOWED_HOSTS = ['domain.railway.app']
CSRF_TRUSTED_ORIGINS = ["https://domain.railway.app"]
```

## 7. Configurar archivos estaticos
```python
# 1
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # cargar whitenoise para renderizar estilos despues de .staticfiles
    "whitenoise.runserver_nostatic",
]
# 2
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
	# Poner whitenoise despues de eso
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
# 3
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```