# 01. Instalando e configurando o MYSQL

História do SQL:
- Desenvolvida no começo dos anos 70, na Califórnia, em um projeto chamado *System R* da IBM (International Business Machines). Cujo objeitvo era comprovar a viabilidade
da implementação de um modelo relacional, proposto por Codd.
- Porém, não era apenas a IBM que estava em busca de formas melhores, a Oracle, dentre outras empresas, também estavam buscando maneiras mais fáceis de manipular
essas estruturas.
- Final dos anos 80 e início dos anos 90, o órgão americano, o ANSI (American National Standart Institute), estabeleceu alguns padrões para as consultas dos bancos
de dados relacionais.
- Portanto, foi criada a linguagem *SQL* (Structured English Query Language). O que torna o aprendizado, a portabilidade, a longevidade, a comunicação e a liberdade
de escolha bem maior. (Obs.: No inglês normalmente se chamam de *SEQUEL*)
- Ao longo do tempo, com o surgimento das redes sociais, precisou-se usar padrões diferentes do banco de dados relacional, o chamado NoSQL.

História do MySQL:
- Criado pelos desenvolvedores, David Axmark, Allan Larsson e Michael Widenius. Buscavam elaborar uma interface SQL que fosse compatível com o que estava surgindo no
mercado de banco de dados. Não encontraram uma solução satisfatória, então, utilizando a linguagem C++, criaram o MySQL.
- Grande vantagem do MySQL é por ser *open source*, apresenta um excelente mecanismo de busca e tarefas.
- Em 2008, o MySQL AB, empresa que gerenciava esse banco de dados, foi comprada por 1 bi de dólares por uma empresa chama *Sun Microsystems* (empresa responsável pela
criação do java). Em 2009, A *Sun Microsystems* foi comprada pela Oracle (que já tinha seu próprio gerenciador de banco de dados).
- Com medo de o MySQL deixar de ser open source, a comunidade criou o MariaDB para evitar isso. Mas, depois, a Oracle manteve o desenvolvimento do MySQL, e hoje
o usuário pode escolher entre a versão gratuita e a versão corporativa que vem com algumas vantagens.

# 02. Manipulando o banco de dados

Schemas = agrupamento de tabelas

No MySQL, database e schemas são tratados como sinônimos.

Selecionando todas as colunas e registros de uma tabela:
        
    Select * from <tabela>
Criando um BD:

    CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] <db_name>
    [create_option] ...
Apagando um BD:

    DROP {DATABASE | SCHEMA} [IF EXISTS] <db_name>
Usando um BD:

    USE <db_name>;
Mostrando os BDs:

    SHOW DATABASES;

Utilizando o MySQL pelo prompt de comando:
- cd\
- cd "Arquivos e Programas" (ou "Program Files")
- cd MySQL
- cd "MySQL Server 8.0"
- cd bin
- mysql -h localhost -u root -p
- < senha >
(para sair digite EXIT)

# 03. Gerenciando as tabelas do banco de dados
Valores INT:
| Tipo |	Valor em Bytes |	Menor Valor(Com Sinal) - Signed |	Menor Valor (Sem Sinal) - Unsigned |	Maior Valor (Com Sinal) - Signed |	Maior Valor (Sem Sinal) - Unsigned |
| --- | --- | --- | --- | --- | --- |
| TINYINT |	1 |	-128 |	0 |	127 |	255 |
| SMALLINT |	2 |	-32768 |	0 |	32767 |	65535 |
| MEDIUMINT |	3 |	-8388608 |	0 |	8388607 |	16777215 |
| INT |	4 |	-2147483648 |	0 |	2147483647 |	4294967295 |
| BIGINT |	8 |	-2xE63 |	0 |	2xE63-1 |	2xE64-1 |

**Ponto Flutuante:**

FLOAT - Precisão simples (4 bytes)

DOUBLE - Precisão dupla (8 bytes)

exemplo: FLOAT(7,4), se inclui 999,00009, vai ser armazenado 999,0001

**Fixos:**

DECIMAL ou NUMERIC

tamanho: Até 65 digitos

exemplo: DECIMAL(5,2) iremos poder armazenar valores entre -999,99 e 999,99, sem possibilidade de arredondamento

**Único:**

BIT

tamanho: Até 64 bits

exemplo: 

BIT(1) - só pode ser 1 ou 0

BIT(2) - só pode ser 01, 10, 00 ou 11

**Atributos dos campos numéricos:**

SIGNED ou UNSIGNED - Vai possuir ou não sinal no número

ZEROFILL - Preenche com Zeros os espaços, exemplo: INT(4). Se armazenarmos 5, será gravado 0005

AUTO_INCREMENT - Sequencia auto incrementada, exemplo: 1, 2, 3, 4, 5, ...

Obs.: Erro OUT OF RANGE, ocorre quando os valores estourarem os limites.

**Data e Hora:**
- DATE - 1000-01-01 até 9999-12-31
- DATETIME - 1000-01-01 00:00:00 até 9999-12-31 23:59:59
- TIMESTAMP - 1970-01-01 00:00:01 UTC até 2038-01-19 UTC (inclui fuso-horários)
- TIME - -838:59:59 e 839:59:59
- YEAR - 1901 até 2155 (pode ser expresso no formato de 2 ou 4 dígitos)

**Strings:**
- CHAR - Cadeia de caracteres com valor fixo (de 0 a 255).
- VARCHAR - Cadeia de cracteres com valor variado (de 0 a 255).
CHAR(4) - "aa" - "  aa"

VARCHAR(4) - "aa" - "aa"

- BLOB (binário):
  - TINYBLOB, BLOB, MEDIUMBLOB, LONGBLOB
- TEXT (texto longo):
  - TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT

**SPACIAL:** (são novidades pros bancos de dados, gráficos e etc)
- GEOMETRY
- POINT
- LINESTRING
- POLYGON

Criando tabelas:

    CREATE TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)
    [table_options]
    [partition_options]
Exemplo simples:

    CREATE TABLE tbCliente
    (CPF CHAR(11),
    NOME VARCHAR(100),
    ENDERECO1 VARCHAR(150),
    ENDERECO2 VARCHAR(150),
    BAIRRO VARCHAR(50),
    CIDADE VARCHAR(50),
    ESTADO VARCHAR(50),
    CEP VARCHAR(8),
    IDADE SMALLINT,
    SEXO VARCHAR(1),
    LIMITE_CREDITO FLOAT,
    VOLUME_COMPRA FLOAT,
    PRIMEIRA_COMPRA BIT(1)
    )
Desafio: Nosso sistema de vendas tem mais uma tabela a ser criada: vendedores.

Algumas informações:

Nome da tabela deve ser TABELA_DE_VENDEDORES
Vendedor tem o número interno da matrícula, onde será armazenado no campo MATRICULA, que deve ser um string de 5 posições.
O nome do vendedor deverá ser armazenado no campo NOME, e deve ser um string de 100 posições.
Criar o campo PERCENTUAL_COMISSAO que representa quantos % de comissão o vendedor ganha sobre cada venda.

Resposta:

    CREATE TABLE TABELA_DE_VENDEDORES (
      MATRICULA VARCHAR(5),
      NOME VARCHAR(100),
      PERCENTUAL_COMISSAO FLOAT)

Apagando uma tabela:

    DROP TABLE <tb_nome>;
OBS.: se você quer apagar ou criar uma tabela de um banco de dados que você não está usando:

    DROP TABLE <bd_nome>.<tb_nome>;

 # 04. Manutenção dos dados nas tabelas
Inserindo dados na tabela:

    INSERT INTO <tb_nome> (
      [colun_1, colun_2, ...] ) VALUES 
      ([val_1, val_2, ...] );
Inserindo mais de um registro em uma tabela:

    INSERT INTO <tb_nome> (
      [colun_1, colun_2, ...] ) VALUES 
      ([val_1, val_2, ...] ),
      ([val_1, val_2, ...] ), ... ;
Alterando registros:

    UPDATE <tb_nome> SET <col> = <mudança>, ...
    WHERE <condição>
Excluindo registros:

    DELETE FROM <tb_nome> WHERE <condição>
