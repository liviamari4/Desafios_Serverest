# PLANO-DE-TESTES — ServeRest API

## 1. Objetivo da suíte

Validar os principais endpoints da API ServeRest, garantindo o funcionamento correto dos fluxos de Usuários, Login e Produtos, com cobertura de cenários positivos e negativos.

---

## 2. Estratégia

* Tipo de teste: Testes de API (caixa-preta)
* Camada: Integração (requisições HTTP)
* Ferramentas: Python, Pytest e Requests
* Abordagem:

  * Testes automatizados de endpoints REST
  * Validação de status code e resposta da API
  * Uso de dados dinâmicos para evitar conflitos entre execuções

---

## 3. Escopo

### Dentro do escopo

* Usuários (/usuarios)
* Login (/login)
* Produtos (/produtos)
* Cenários positivos e negativos

### Fora do escopo

* Testes de performance
* Testes de segurança avançada
* Testes de interface (UI)
* Carrinho (/carrinhos)

---

## 4. Cenários por endpoint

### Usuários (/usuarios)

* Listar usuários
* Cadastrar usuário válido
* Cadastrar usuário com e-mail duplicado
* Cadastrar usuário com campos obrigatórios faltando
* Buscar usuário por ID válido
* Buscar usuário por ID inexistente
* Atualizar usuário
* Excluir usuário

---

### Login (/login)

* Login com credenciais válidas
* Login com senha incorreta
* Login com email inexistente
* Login com campos vazios

---

### Produtos (/produtos)

* Listar produtos
* Buscar produto por ID válido
* Buscar produto por ID inexistente
* Cadastrar produto com token de administrador
* Cadastrar produto sem token de administrador
* Atualizar produto
* Excluir produto

---

## 5. Critérios de qualidade

Um teste é considerado válido quando:

* Valida o status code esperado
* Valida a estrutura mínima da resposta
* É independente (não depende da execução de outro teste)
* Utiliza dados dinâmicos quando necessário
* Pode ser executado várias vezes sem conflito de dados
