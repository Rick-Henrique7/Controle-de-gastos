# Controle de Gastos Pessoais

Uma aplicação web para controle financeiro pessoal, permitindo ao usuário cadastrar despesas e receitas, categorizar movimentações e visualizar relatórios financeiros mensais. O objetivo é oferecer uma forma simples e intuitiva de gerenciar o orçamento.

---

## ✨ Funcionalidades

- **Cadastro de Despesas e Receitas:**  
  Permite registrar valor, descrição, data e categoria.

- **Edição e Exclusão de Movimentações:**  
  Gerencie facilmente seus lançamentos.

- **Filtragem Avançada:**  
  Filtre por período (mês/ano) e categoria.

- **Categorias Padrão e Personalizadas:**  
  Utilize categorias como Alimentação, Transporte, Lazer, Saúde, Educação ou crie suas próprias.

- **Relatórios Mensais:**  
  Visualize total de receitas, despesas e saldo.

- **Gráficos Interativos:**  
  Distribuição de gastos por categoria (pizza, barras).

- **Exportação em PDF:**  
  Gere relatórios em PDF com um clique.

- **(Futuro) Cadastro de Usuários:**  
  Salve dados individualmente com login.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Flask (Python)
- **Banco de Dados:** SQLite (versão inicial), com possibilidade de migração para PostgreSQL
- **Frontend:** Responsivo, acessível em computador e celular

---

## 📋 Requisitos

### Funcionais

- Cadastro, edição e exclusão de despesas e receitas
- Filtragem por período e categoria
- Categorias padrão e personalizadas
- Relatórios mensais e gráficos
- Exportação de relatórios em PDF
- (Opcional) Cadastro de usuários

### Não Funcionais

- Interface simples e intuitiva
- Responsividade
- Segurança básica (validação de dados, prevenção de SQL Injection)
- Deploy em Render/Heroku/Railway

### Qualidade

- Tempo de resposta inferior a 3 segundos
- Suporte a até 1.000 registros sem perda significativa de desempenho

---

## 🚀 Casos de Uso

- **Cadastrar uma despesa:**  
  Informe valor, data, descrição e categoria. O sistema salva no banco.

- **Visualizar relatórios:**  
  Selecione um mês e veja receitas, despesas, saldo e gráficos.

- **Exportar relatório:**  
  Clique em "Exportar PDF" para gerar o arquivo.

---

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/controle-de-gastos.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd controle-de-gastos
   ```

3. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

6. Inicie o servidor:
   ```bash
   flask run
   ```

Acesse a aplicação em `http://127.0.0.1:5000`.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👥 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues.

---

## 📝 Notas Finais

Este é um projeto em andamento. Recursos adicionais e melhorias estão planejados para versões futuras. Fique à vontade para sugerir funcionalidades!
