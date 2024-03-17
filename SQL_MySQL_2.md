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

