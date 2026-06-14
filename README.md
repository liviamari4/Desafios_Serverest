# Desafios_Serverest

## Descrição

Projeto desenvolvido para automatizar testes da API ServeRest utilizando Python, Pytest e Requests.

Foram implementados testes automatizados para os endpoints de Usuários e Produtos da API ServeRest, cobrindo cenários de sucesso e erro.

## Tecnologias Utilizadas

- Python
- Pytest
- Requests

## Estrutura do Projeto

```text
desafio-serverest/
│
├── tests/
│   ├── test_users.py
│   ├── test_products.py
│
├── PLANO-DE-TESTES.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Cenários Testados

### Usuários

- Listar usuários
- Cadastrar usuário válido
- Cadastrar usuário com e-mail duplicado
- Cadastrar usuário com campos faltando
- Buscar usuário por ID
- Buscar usuário com ID inválido
- Atualizar usuário
- Excluir usuário
- Cadastrar usuário com e-mail inválido
- Cadastrar usuário com nome vazio

### Produtos

- Listar produtos
- Buscar produto com ID inválido

## Documentação

O planejamento da suíte de testes está documentado no arquivo:

- PLANO-DE-TESTES.md

## Como Executar

### Clonar o repositório

```bash
git clone https://github.com/liviamari4/Desafios_Serverest.git
```

### Acessar a pasta do projeto

```bash
cd Desafios_Serverest
```

### Criar o ambiente virtual

```bash
python -m venv .venv
```

### Ativar o ambiente virtual (Windows)

```bash
.venv\Scripts\activate
```

### Instalar as dependências

```bash
pip install -r requirements.txt
```

### Executar os testes

```bash
pytest -v
```

## API Utilizada

https://compassuol.serverest.dev/
