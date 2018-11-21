psql -c "drop database cabChoice;" &&
psql -c "create database cabChoice;" &&
rm main/migrations/* &&
touch main/migrations/__init__.py &&
./manage.py makemigrations &&
./manage.py migrate &&
./manage.py init
