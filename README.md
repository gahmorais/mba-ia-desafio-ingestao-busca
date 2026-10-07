# Desafio MBA Engenharia de Software com IA - Full Cycle

* Foi necessário realizar o upgrade da biblioteca psycopg-binary da versão 3.2.9 para a versão 3.2.10, devido ao seguinte erro
ERROR: Could not find a version that satisfies the requirement psycopg-binary==3.2.9 (from versions: 3.2.10, 3.2.11, 3.2.12, 3.2.13, 3.3.0, 3.3.1, 3.3.2, 3.3.3, 3.3.4)

* utilizar a versão 3.11.15 do python, utilizar uma versão mais nova pode fazer o projeto quebrar devido a biblioteca que não tem wheel para python 3.14 como a psycopg2-binary, por exemplo.

Para execução do projeto siga os seguintes procedimentos

`docker compose up -d` -> Inicialização dos containers
* postgres
* pgvector 
* adminer (visualização dos dados.)

`pip install -r requirements.txt` -> Instalação de dependências do projeto

`python src/ingest.py` -> Realizará o processamento do document.pdf e a criação dos chunks no banco de dados

`python src/chat.py` -> Inicializa o chat interativo, cada pergunta apresenta uma resposta de acordo com o contexto do projeto, para encerrar o chat digite 'sair'.

Neste projeto foi observado que para o rag para o k=10 tem uma limitação estrutural associada a busca por similaridade, ao definir o k=10 filtramos um trecho pequeno dos dados e perguntas como 