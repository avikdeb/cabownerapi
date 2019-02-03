psql -c "drop database roamCab;" &&
psql -c "create database roamCab;" &&
rm main/migrations/* &&
touch main/migrations/__init__.py &&
./manage.py makemigrations &&
./manage.py migrate &&
./manage.py init
