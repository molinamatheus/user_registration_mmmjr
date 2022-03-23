# USER REGISTRATION

## Objetivo:
Construir pelo menos dois endpoints utilizando Django:
  - Cadastrar usuário, fornecendo o login, senha e data de nascimento
  - Senha deixar como opcional, se não fornecido gerar uma senha aleatória.
  - Consultar usuários cadastrados.
  - Deve ser possível consultar em XLSX, CSV ou JSON.

## O que precisa instalar?
- Instalar Django, Django-rest-framework e Insomnia
Obs.: O insomnia é opcional, mas eu usei ele para testar

## Como testar a aplicação?
Utilizei o Insomnia para isso, e segui os seguintes passos:
- Criar uma request POST
- Colocar o seguinte caminho: http://127.0.0.1:8000/users/
- Escolher o </>TEXT JSON
- Usar o seguinte modelo para criação de um novo usuário:
  {
	"username": "user",
	"email": "user@email.com",
	"password": "SENHA É OPCIONAL, NÃO PRECISA POR NADA SE QUISER",
	"birthday": "1999-05-05"
  }
- Clicar em Send
- Visualizar o resultado em PREVIEW
- Como na imagem abaixo.
![img](https://user-images.githubusercontent.com/99224273/159698054-7ab38814-d1ca-4719-bfc1-5f49a39f2f93.png)
