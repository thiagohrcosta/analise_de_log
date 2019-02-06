# !/usr/bin/env python2
# encoding: utf-8

# Importando psycopg2 para conectar-se ao banco de dados

import psycopg2

# Aplicando uma função para chamada posterior do Banco de Dados

DBNAME = "news"


def executar_db(query):

    """OBJETIVO: Conectar-se ao banco de dados, e executar a pesquisa
    retornando os resultados"""

    db = psycopg2.connect('dbname=' + DBNAME)

    c = db.cursor()

    c.execute(query)

    rows = c.fetchall()

    db.close()

    return rows

# PERGUNTAS E RESPOSTAS


def artigos_mais_visualizados():

    """OBJETIVO: Função com o objetivo de retornar os três artigos mais
    populares de todos os tempos. Informação apresentada como uma lista
    organizada com o artigo mais popular no topo"""

    # Construção da Query

    query = """

        SELECT articles.title, COUNT(*) AS num

        FROM articles

        JOIN log

        ON log.path LIKE concat('/article/%', articles.slug)

        GROUP BY articles.title

        ORDER BY num DESC

        LIMIT 3;

    """

    # Execução da Query

    results = executar_db(query)

    # Função para imprimir os resultados de 'def artigos_mais_visualizados()'

    print('Os artigos mais populares são: \n')

    count = 1

    for i in results:

        number = '(' + str(count) + ') "'

        title = i[0]

        views = '" com ' + str(i[1]) + " visualizações"

        print(number + title + views)

        count += 1


def autores_mais_populares():

    """OBJETIVO: Organização de todos os artigos que cada autor
    escreveu, e indicação de quais obtiveram maior visualização.
    A informação é apresentada como uma lista organizada com o
    autor mais popular no topo"""

    # Construção da Query

    query = """

        SELECT authors.name, COUNT(*) AS num

        FROM authors

        JOIN articles

        ON authors.id = articles.author

        JOIN log

        ON log.path like concat('/article/%', articles.slug)

        GROUP BY authors.name

        ORDER BY num DESC

        LIMIT 3;

    """

    # Execução da Query

    results = executar_db(query)

    # Função para Impressão dos resultados de 'def autores_mais_populares()':

    print('Os autores mais populares de todos os tempos são: \n')

    count = 1

    for i in results:

        print('(' + str(count) + ') ' + i[0] + ' com ' + str(i[1]) +
              " visualizações")

        count += 1


def dias_com_mais_de_1_por_cento_de_erro():

    """OBJETIVO: Indicar por meio da tabela de logs o status HTTP que
    o site de notícias enviou ao navegador do usuário. Neste caso páginas
    com erro."""

    # Construção da Query

    query = """

        SELECT total.day,

          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent

        FROM (

          SELECT date_trunc('day', time) "day", count(*) AS error_requests

          FROM log

          WHERE status LIKE '404%'

          GROUP BY day

        ) AS errors

        JOIN (

          SELECT date_trunc('day', time) "day", count(*) AS requests

          FROM log

          GROUP BY day

          ) AS total

        ON total.day = errors.day

        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)

        ORDER BY percent DESC;

    """

    # Execução da Query

    results = executar_db(query)

    # Impressão dos Resultados

    print('Em quais dias mais de 1% das requisições resultaram'
          'em erros? \n')

    for i in results:

        date = i[0].strftime('%B %d, %Y')

        errors = str(round(i[1]*100, 1)) + "%" + " erros"

        print(date + " -- " + errors)

# IMPRESSÃO DOS RESULTADOS NA TELA

print('Imprimindo o resultado da pesquisa:')
print('====================================')
artigos_mais_visualizados()
print('====================================')
autores_mais_populares()
print('====================================')
dias_com_mais_de_1_por_cento_de_erro()
