# Desafio MBA Engenharia de Software com IA - Full Cycle

* Foi necessário realizar o upgrade da biblioteca psycopg-binary da versão 3.2.9 para a versão 3.2.10, devido ao seguinte erro
ERROR: Could not find a version that satisfies the requirement psycopg-binary==3.2.9 (from versions: 3.2.10, 3.2.11, 3.2.12, 3.2.13, 3.3.0, 3.3.1, 3.3.2, 3.3.3, 3.3.4)

* utilizar a versão 3.11.15 do python, utilizar uma versão muito nova pode fazer o projeto quebrar devido a bibliotecas que não tem wheel para python 3.14 como a psycopg2-binary, por exemplo.