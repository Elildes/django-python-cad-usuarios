# Projeto Web Application com HTML usando Python e com o framework Django

## Criar projeto e aplicação Cadastro de Usuários

**Criar projeto cadastro de usuários**  

```
mkdir projeto-python-django
django-admin startproject projeto_cad_usuarios
cd .\projeto_cad_usuarios\
```

**Criar repositório local do Git**  

```
git init
git add *
git commit -m "create project python with django"
git config user.email "<seu_email>" && git config user.name "<seu_nome>"
git commit -m "create project python with django"
```

**Comandos diversos**  

No terminal é possível aplicar vários comandos no desenvolvimento da aplicação web com o framework Django.

`cd .\projeto_cad_usuarios\`  
`python .\manage.py runserver` - roda o server  
`python .\manage.py makemigrations` - roda o banco de dados  
`python .\manage.py migrate`

. Adicionando as alterações no repo git:  
```
git add *
git commit -m "create: rota, views, html, models, migrations and database sqlite"
```

