# Web Scraper - Top 10 Séries do IMDb

Este projeto é um **Web Scraper em Python** que coleta as **10 séries mais bem avaliadas do site IMDb**.  
O objetivo é mostrar como utilizar as bibliotecas `requests` e `BeautifulSoup` para extrair informações de páginas web.

---

## Funcionalidades

- Acessa a página de **Top 250 Séries** do IMDb.
- Extrai os **10 primeiros títulos** da lista.
- Captura também a **nota (rating)** de cada série.
- Exibe os dados organizados no terminal.

Exemplo de saída esperada:
Breaking Bad ⭐ 9.5
Band of Brothers ⭐ 9.4


## Tecnologias usadas

- [Python 3.x](https://www.python.org/)
- [Requests](https://docs.python-requests.org/en/latest/) → para baixar o conteúdo da página.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) → para analisar e extrair informações do HTML.
---

## Estrutura do Projeto

webscraper-imdb-series/
│── scraper.py # Código principal do scraper
│── requirements.txt # Dependências do projeto
│── README.md # Documentação do projeto


---

## Como executar o projeto

1. **Clone este repositório**  
   ```bash
   git clone https://github.com/seuusuario/webscraper-imdb-series.git
   cd webscraper-imdb-series

2. **Crie e ative um ambiente virtual (opcional, mas recomendado)**

No Linux/Mac:
python -m venv venv
source venv/bin/activate


No Windows:
python -m venv venv
venv\Scripts\activate

3. **Instale as dependências**
pip install -r requirements.txt


4. **Execute o scraper**
python scraper.py

## Autor

- Nome: Ana Beatriz Gonçalves Alves
- Curso: Inteligência Artificial – FATEC
- Disciplina: Linguagem de Programação II
- Professor: Prof. Orlando Saraiva Júnior
