web: gunicorn Booker_Back.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
reserva: python reservas_views.py