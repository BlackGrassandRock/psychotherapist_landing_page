DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', 5431),
        'OPTIONS': {
            'options': '-c search_path=public,content'
        }
    }
}


# docker run -d   --name postgres   -p 54
# 31:5432   -v $HOME/postgresql/data:/var/lib/postgresql/data   -e POSTGRES_PASSWORD=Sasha2000.S   -e POSTGRES_USER=app   -e POSTGRES_DB=work_psycho_database    postgres:16
