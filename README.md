# DashBoard Ibovespa

## Descrição
Nesse repositório existem 2 DashBoards:
- Dashboard.py ( DashBoard Simples com gráfico de candles da cotação do ativo ) requirements1.txt
- Dashboard_plus.py ( Igual Dashboard.py porém faz Análise de Sentimentos da nóticias ) requirements2.txt

## Melhorias:
- Criar uma base de dados, a fim de evitar o alto número de requests
- Pegar nome das empresas por meio do yfinance, automizando a busca no site (https://braziljournal.com/)
- No caso DashBoard_plus, Utilizar outras apis de Análise de Sentimento como: GPT4 (model='text-davinci=003') e FinBert (Do HuggingFace https://huggingface.co/yiyanghkust/finbert-tone)

## Contato
https://linktr.ee/bernardoalemar


# Executar o Script em sua máquina local
## Pré-requisitos:

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- Python 3.10.12
- pip (gerenciador de pacotes Python)
- Git (ferramenta de controle de versão)

Uma vez que você tenha isso instalado, abra um terminal em sua máquina local e execute os seguintes comandos:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/DashBoard-Ibovespa.git

2. **Navegue até o diretório do repositório clonado:**
   ```bash
   cd DashBoard-Ibovespa

3. **Crie um ambiente virtual:**
   ```bash
    python -m venv ambiente_virtual

4. **Ative o ambiente virtual:**

   **4.1 Linux**
   ```bash
    source ambiente_virtual/bin/activate
   ```
   **4.2 Windows**
   ```bash
    source ambiente_virtual\Scripts\activate

5. **Instale as Dependências:**
- Instale de acordo com Dashboard que deseja utilizar.
   ```bash
    pip install -r requeriments.txt 

