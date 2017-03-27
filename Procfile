web: gunicorn mysite.wsgi
web: python website3/manage.py collectstatic --noinput; bin/gunicorn --workers=4 --bind=0.0.0.0:$PORT mysite/settings.py