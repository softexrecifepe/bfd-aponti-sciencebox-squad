# Instala as dependências
pip install -r requirements.txt

# Garante que o WhiteNoise e o Django consigam criar os arquivos
python3.12 manage.py collectstatic --noinput --clear

echo "BUILD FINALIZADO COM SUCESSO"