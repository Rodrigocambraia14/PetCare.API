# README

## Descrição da Aplicação

Esta é uma API em Python Flask que permite aos usuários registrar seus pets, gerenciar seu calendário de vacinação e ver curiosidades. A API utiliza o Swagger para documentação e teste de endpoints.

## Como Executar

1. Certifique-se de ter o Python instalado. Você pode fazer o download em [python.org](https://www.python.org/).

2. Clone este repositório para o seu ambiente local:

    ```
    git clone https://github.com/Rodrigocambraia14/PetCare.API.git
    ```

3. Navegue até o diretório do projeto:

    ```
    cd PetCare.API
    ```

. Ative o ambiente virtual:

    - No Windows:

    ```
    venv\Scripts\activate
    ```

    - No macOS e Linux:

    ```
    source venv/bin/activate
    ```

5. Execute o aplicativo Flask:

    ```
    python app.py
    ```

6. Acesse a documentação Swagger em seu navegador, geralmente em `http://localhost:5000/swagger`, para visualizar e testar os endpoints disponíveis.

## Requirements

bcrypt==4.1.2
blinker==1.7.0
click==8.1.7
colorama==0.4.6
Flask==3.0.2
Flask-Cors==4.0.0
flask-swagger-ui==4.11.1
itsdangerous==2.1.2
Jinja2==3.1.3
MarkupSafe==2.1.5
schedule==1.2.1
Werkzeug==3.0.1


## Observações

1. Este projeto é apenas um MVP, portanto, não possui recursos como autenticação JWT, OAuth2, endpoints de funcionalidades complexas e afins.

## Exemplo de Uso

1. Autentique utilizando o usuário da seed: tester@PUCRIO.com e a senha: PUC@123
1. Registre um pet utilizando o endpoint **POST /pets/add**.
2. Cadastre um evento no calendário de vacinação utilizando o endpoint **POST /vaccine_calendar/add_**.

## Executando com Docker
Para facilitar o processo de configuração e execução do projeto, você pode usar o Docker. Siga os passos abaixo para rodar a aplicação com Docker:

### Passo 1: Criar imagem
Execute o seguinte comando na raiz do projeto:

```sh
docker build -t python-docker .
```

### Passo 2: Execute o container docker utilizando a imagem criada anteriormente

```sh
docker run -p 5001:5000 python-docker
```

### Acesse  a aplicação no endereço disponibilizado

http://localhost:5001

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
