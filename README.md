#PROJETO 3 : ANÁLISE DE LOG
Terceiro projeto apresentado ao curso *NANODEGRE - Desenvolvimento Web Full Stack* ministrado pela UDACITY.

##Descrição do Projeto
O objetivo é desenvolver utilizando a linguagem Python um código capaz de analisar, tratar e imprimir dados de um banco de dados em uma lista ordenada. Para tanto fora utilizado o Python com Psycopg2. 

##Questões a serem respondidas no projeto:
1.  **Quais são os três artigos mais populares de todos os tempos?** Quais artigos foram os mais acessados? Apresente esta informação como uma lista organizada com o artigo mais popular no topo.
2. **Quem são os autores de artigos mais populares de todos os tempos?** Isto é, quando você organizar todos os artigos que cada autor escreveu, quais autores obtiveram mais views? Apresente esta informação como uma lista organizada com o autor mais popular no topo.
3. **Em quais dias mais de 1% das requisições resultaram em erros?** A tabela de logs inclui um status de coluna que indica o código de status HTTP que o site de notícias enviou ao navegador do usuário (consulte novamente esta aula se você quiser rever a ideia dos códigos de status HTTP).

#COMO EXECUTAR O PROJETO - ANÁLISE DE LOG
Para executar o presente projeto você deverá previamente seguir os passos abaixo:

1. Instalar o [Vagrant](https://www.vagrantup.com/);
2. Instale Máquina Virtual - [VirtualBox](https://www.virtualbox.org/);
3. Efetue do download do arquivo vagrant original do Udacity [Vagrant](https://github.com/udacity/fullstack-nanodegree-vm
);
4. Baixe o banco de dados [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip);
5. Extraia o arquivo newsdata.zip e o coloque no diretório Vagrant compartilhado;
6. Efetue o download do arquivo deste projeto analiselog.py e copie-o para a pasta Vagrant

**Inicie a máquina virtual**

7. Para iniciar a máquina virtual efetue o download do [GitBash](https://git-scm.com/downloads)
8. Inicie o **GitBash** e vá até o diretório onde se encontra a pasta vagrant, por exemplo:

C:> cd python 27
C:> python27> cd FSND-Virtual-Machine
C:> python27>FSND-Virtual-Machine> cd /vagrant
C:> python27>FSND-Virtual-Machine>vagrant>

9. Dentro do diretório vagrant ative a máquina virtual com o comando **vagrant up** ;
10. Após a sua ativação, digite o comando **vagrant ssh** para ativar a sua máquina virtual.
11. Carregue o banco de dados com o comando **psql -d news -f newsdata.sql;
12. Execute no **GitBash** o comando **python analiselog.py** para executar o relatório.

#RESULTADO ESPERADO:
Imprimindo o resultado da pesquisa:
====================================
Os artigos mais populares são:

(1) "Candidate is jerk, alleges rival" com 338647 visualizações
(2) "Bears love berries, alleges bear" com 253801 visualizações
(3) "Bad things gone, say good people" com 170098 visualizações
====================================
Os autores mais populares de todos os tempos são:

(1) Ursula La Multa com 507594 visualizações
(2) Rudolf von Treppenwitz com 423457 visualizações
(3) Anonymous Contributor com 170098 visualizações
====================================
Em quais dias mais de 1% das requisições resultaramem erros?

July 17, 2016 -- 2.3% erros
