# 1. Descrição Geral

O sistema será uma **aplicação web para controle financeiro pessoal**, permitindo que o usuário cadastre suas despesas e receitas, categorize-as e visualize relatórios financeiros mensais.  
O objetivo é oferecer uma forma **simples e intuitiva** de gerenciar o orçamento.

---

# 2. Requisitos Funcionais (RF)

## 🔹 Cadastro e Gerenciamento de Movimentações

- **RF01:** O sistema deve permitir cadastrar despesas com: valor, descrição, data e categoria.
- **RF02:** O sistema deve permitir cadastrar receitas com: valor, descrição, data e categoria.
- **RF03:** O sistema deve permitir editar e excluir movimentações cadastradas.
- **RF04:** O sistema deve permitir filtrar movimentações por período (ex: mês/ano) e categoria.

## 🔹 Categorias e Organização

- **RF05:** O sistema deve disponibilizar categorias padrão (ex: Alimentação, Transporte, Lazer, Saúde, Educação).
- **RF06:** O sistema deve permitir ao usuário criar suas próprias categorias.

## 🔹 Relatórios e Dashboard

- **RF07:** O sistema deve gerar um relatório mensal com total de receitas, despesas e saldo.
- **RF08:** O sistema deve exibir gráficos de distribuição de gastos por categoria (ex: pizza, barras).
- **RF09:** O sistema deve permitir exportar relatórios em PDF.

## 🔹 Usuários (futuro opcional)

- **RF10:** O sistema poderá permitir cadastro de usuários com login, para salvar dados individualmente (pode ser implementado em versão 2).

---

# 3. Requisitos Não Funcionais (RNF)

- **RNF01:** O sistema deve ser responsivo (acessível em computador e celular).
- **RNF02:** O sistema deve ter interface simples e intuitiva.
- **RNF03:** O sistema deve utilizar Flask (Python) para o backend.
- **RNF04:** O banco de dados deve ser SQLite (para versão inicial) e possibilitar migração para PostgreSQL.
- **RNF05:** O sistema deve seguir boas práticas de segurança básica (validação de dados e prevenção de SQL Injection).
- **RNF06:** O sistema deve estar disponível para deploy em Render/Heroku/Railway.

---

# 4. Requisitos de Qualidade

- O tempo de resposta das páginas deve ser **inferior a 3 segundos** em rede padrão.
- O sistema deve suportar **até 1.000 registros de movimentações** sem perda significativa de desempenho.

---

# 5. Casos de Uso (simplificados)

- **Cadastrar uma despesa:**  
  O usuário informa valor, data, descrição e categoria. O sistema salva no banco.

- **Visualizar relatórios:**  
  O usuário seleciona um mês e o sistema mostra receitas, despesas, saldo e gráficos.

- **Exportar relatório:**  
  O usuário clica em "Exportar PDF" e o sistema gera
<div align="center">
<img src="https://github.com/user-attachments/assets/08d81c8d-65c7-4193-a1d6-956e80b74cc0" width="400px" />
</div>
