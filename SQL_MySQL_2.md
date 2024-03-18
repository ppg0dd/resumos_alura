# 01. Configurando ambiente e conhecendo SQL
Conteúdo presente no SQL_MySQL_1

# 02. Filtrando as consultas de dados
Database -> Reverse Engineer

Serve para modelar um banco de dados físico.

Operadores lógicos:
- AND
- OR
- NOT
- IN (contém)  (ex.: sabor in ('Laranja', 'Manga'),   isso retorna todos os registros com sabores laranja ou manga)
- BETWEEN
- LIKE (ex.: NOME LIKE %SOARES%, retorna todos os nomes que contém soares)

# 03. Apresentação dos dados de uma consulta

DISTINCT = Retorna apenas os campos diferentes em uma tabela.
    
    SELECT DISTINCT EMBALAGEM, TAMANHO FROM tbproduto;
    # Seleciona os registros em que a combinação entre embalagem e tamanho não se repitam

LIMIT = limita o número de linhas exibidas

    SELECT * FROM <tb> 
    LIMIT 4; # a contagem começa pelo numero 1
Também é possível escolher alguns específicos: 

    LIMIT 2,3 # A partir do 2 (começa pelo 0) ele vai selecionar os 3 próximos (incluindo o 2)

ORDER BY = define qual vai ser a ordem dos registros pelos campos.

    SELECT * FROM <tab> ORDER BY <campo> <tipo da ordem (opcional)>
Tipos:
- ASC (Ascendente)
- DESC (Decrescente)

GROUP BY = Apresenta o resultado agrupando valores numéricos por uma chave de critério.

    SELECT <col_1>, SUM(<col_2>) FROM <tab> GROUP BY <col_1>
Podemos usar:
- SUM (soma)
- MAX (máximo)
- MIN (mínimo)
- AVG (média)
- COUNT (conta ocorrências)
Obs.: quando você apenas utiliza a coluna usada para somar, média, etc. Você não precisa usar o GROUP BY

HAVING = Filtro (como um WHERE) usado após o agrupamento.

    SELECT <col_1>, SUM(<col_2>) FROM <tab>
    GROUP BY <col_1> HAVING SUM(<col_2>) > 20;
CASE = Fazemos um teste em um ou mais campos e, dependendo do resultado, teremos um ou outro valor.

    CASE
      WHEN <condição1> THEN <Valor1>
      WHEN <condição2> THEN <Valor2>
      (...)
      WHEN <condiçãoN> THEN <ValorN>
      ELSE <valorElse>
    END

EXEMPLO PRÁTICO:

    SELECT NOME,
    CASE 
        WHEN YEAR(data_de_nascimento) < 1990 THEN 'Velhos'
        WHEN YEAR(data_de_nascimento) BETWEEN 1990 AND 1995 THEN 'Jovens' 
        ELSE 'Crianças' 
    END  AS "CLASSIFICAÇÃO POR IDADE"
    FROM tabela_de_clientes;

# 04. Juntando tabelas e consultas

JOINs -> Possibilidade de unir uma ou mais tableas através de campos em comum

Tipos de Join:

INNER JOIN = Retorna somente quando temos chaves correspondentes

    SELECT A.NOME, B.HOBBY
    FROM TABELA_ESQUERDA A INNER JOIN TABELA_DIREITA B
    ON A.IDENTIFICADOR = B.IDENTIFICADO;
LEFT JOIN = Retorna todos da tabela da esquerda e somente os correspondentes na da direita. (quem não tem correspondência fica NULL)
RIGT JOIN = Retorna todos da tabela da direita e somente os correspondentes na da esquerda.

FULL JOIN = Retorna todos os registros de todas as tabelas

CROSS JOIN = Retorna o produto cartesiano das duas tabelas (todas as combinações possíveis de correspondência)

    SELECT A.NOME, B.HOBBY
    FROM TABELA_ESQUERDA A CROSS JOIN TABELA_DIREITA B;
