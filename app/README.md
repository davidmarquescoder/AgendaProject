[======Verificações no git======]
Verificar em qual branch estou trabalhando: git branch
Configurar o .gitignore

[======Configurações do ambiente virtual======]
Criar meu ambiente virtual usando: python -m venv venv
Ativar meu ambiente virtual usando: .\venv\Scripts\Activate.ps1
Instalar o django usando: pip install django

[======Configurações do projeto Django======]
Criar o projeto usando: django-admin startproject project .
Configurar o settings: 
    INSTALLED_APPS;
    TEMPLATES;
    STATICFILES_DIRS

[======Configurações do App======]
Criar o app contact usando: python manage.py startapp contact
Criar pasta: templates
Criar arquivo: urls.py

[======Migrations Commands======]
OBS: QUASE SEMPRE que for realizas alterações no 'models' é necessário usar esses dois comandos na ordem seguinte.
Um para criar uma migração e outro para aplicar a migração, você vai perceber que um arquivo vai ser adicionado
na pasta 'migrations' sempre que fizer isso, essa pasta armazena nossas alterações no banco de dados (models)

python manage.py makemigrations
python manage.py migrate

[======SuperUser Commands======]
python manage.py createsuperuser
python manage.py changepassword USERNAME

[======Registrando nosso model no admin======]