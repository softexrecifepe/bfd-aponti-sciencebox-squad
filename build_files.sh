
pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate

echo "BUILD FINALIZADO COM SUCESSO"