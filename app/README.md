# =======================AJUDA=======================
Em caso de esquecimento dos comandos django, use o comando:
# python manage.py help
Esse comando mostrará todos os comandos possiveis com django

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
#    INSTALLED_APPS;
#    TEMPLATES;
#    STATICFILES_DIRS
#    STATIC_ROOT = BASE_DIR / 'static' #collectstatic
Quando eu usar o comando collectstatic ele criará a pasta static na raiz, é importante jogar isso no .gitignore para não subir pro github

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
Registre o model criado no arquivo admin.py

[======Shell do Django======]
# Qualquer dúvida você pode olhar na aula: 455 da seção 10
Usando o comando: python manage.py shell
é possivel entrar no shell do django e fazer CRUD
com os dados da tabela pelo terminal

Comandos:
# Entre no shell do django usando:
python manage.py shell

# Primeiramente você terá que importar a sua tabela criada no models.py, usando o comando:
from contact.models import Contact

# Criando um contato de forma lazy (Dessa maneira ele cria o contato somente na memória)
contact = Contact(first_name = 'David') | contact.first_name = 'David'

# Caso queira salvar o contato no banco de dados, use o comando abaixo:
contact.save()

# Caso queira deletar o contato salvo do banco de dados use:
contact.delete()

# Com o comando abaixo é possivel armazenar na variável todos contatos que estão na tabela
contact = Contact.objects.all()

# Com o comando abaixo é possivel armazenar na variável todos os contatos da tabela de forma ordenada pelo id de maneira decrescente
contact = Contact.objects.all().order_by('-id')

# Com o comando abaixo é possivel armazenar na variável todos os contatos com primeiro nome de 'José'
contact = Contact.objects.all().filter(first_name = 'José')

# Com o comando abaixo é possivel buscar e armazenar na variável um contato através do seu 'id' (Mas acho que pode ser usado outros parêmtros de busca também além do 'id')
contact = Contact.objects.get(id=2)

# Salvando um novo contato de forma não lazy, esse comando já salva o contato automáticamente no banco de dados (sem necessitar do comando: save())
contact = Contact.objects.create(first_name = 'Marcos', last_name = 'Jucelino', phone = '99991738263')

[======Configurando arquivos de imagens no settings======]
Para o django utilizar imagens, ele precisa da biblioteca 'pillow' então instale ela no ambiente virtual
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

Assim que eu salvar a primeira imagem no banco ele vai criar a pasta 'media' na raiz com a imagem salva

Após isso, precisamos ir no nosso arquivo url.py do prject e concatenar com o urlpatterns as urls do media e do static
Pra isso vamos precisar importar essas urls do arquivos settings usando:
# from django.conf.urls.static import static
# from django.conf import settings
Após isso vamos concatentar:
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
Você pode fazer essa mesma configuração para o static, porém não é necessário, mas caso queira fazer:
# urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

Após fazer as alterações no settings, configurando o static root, media url e media root, você precisa usar o comando:
python manage.py collectstatic isso criará duas pastas a pasta media e a pasta static que precisam ser colocadas no .gitignore