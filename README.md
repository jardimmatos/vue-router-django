# Criar ambiente Virtual
python -m venv venv


#Linux
source venv/bin/activate
#Windows  
source venv/Scripts/activate

# instalar os requisitos
pip install -r requisitos.txt


python manage.py migrate 
