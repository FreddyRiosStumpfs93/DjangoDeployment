import os

# Permite obtener la ruta del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'clasificacion_arancelaria.sqlite3'),
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME' : 'clasificacion_arancelaria',
        'NAME' : 'clasificacion_arancelaria_postgreSQL',
        # 'USER' : 'postgres',
        # 'PASSWORD' : '123',
        'USER' : 'user1',
        'PASSWORD' : 'pass1',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}