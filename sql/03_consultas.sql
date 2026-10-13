-- 1. Contar todos os registros
SELECT COUNT(*)
FROM raw_vendas;


-- 2. Listar as filiais existentes
SELECT DISTINCT "Branch"
FROM raw_vendas;


-- 3. Quantidade de vendas por filial
SELECT
    "Branch",
    COUNT(*) AS quantidade_vendas
FROM raw_vendas
GROUP BY "Branch"
ORDER BY quantidade_vendas DESC;

-- Giza: 328 vendas | Alex: 340 vendas | Cairo: 332 vendas


-- 4. Faturamento por filial
SELECT
    "Branch",
    SUM(CAST("Sales" AS NUMERIC)) AS faturamento
FROM raw_vendas
GROUP BY "Branch"
ORDER BY faturamento DESC;

-- Giza: 110.568,7065 | Alex: 106.200,3705 | Cairo: 106.197,6720 


-- 5. Valor médio das vendas por filial
SELECT
    "Branch",
    AVG(CAST("Sales" AS NUMERIC)) AS media_vendas
FROM raw_vendas
GROUP BY "Branch"
ORDER BY media_vendas DESC;

-- Resultado: Giza 337,10 | Cairo 319,87 | Alex 312,35 
-- Qual filial tem maior ticket médio? Giza com 337,10


-- 6. Menor e maior venda
SELECT
    MIN(CAST("Sales" AS NUMERIC)) AS menor_venda,
    MAX(CAST("Sales" AS NUMERIC)) AS maior_venda
FROM raw_vendas;

-- Resultado Minimo: 10,68   |  Maximo: 1.042,65

-- 7. Listar as cidades existentes
SELECT DISTINCT "City"
FROM raw_vendas;

-- Resultado: Yangon | Naypyitaw | Mandalay

-- 8. Listar as linhas de produto existentes
SELECT DISTINCT "Product line"
FROM raw_vendas;

-- Resultado: Fashion accessories | Electronic acessories | Health and beauty | Food and Beverages | Sports and travel | Home and lifestyle

-- 9. Listar as formas de pagamento existentes
SELECT DISTINCT "Payment"
FROM raw_vendas;

-- Resultado: Credit card | Ewallet | Cash

-- 10. Contar transações por forma de pagamento
SELECT
    "Payment",
    COUNT(*) AS quantidade_transacoes
FROM raw_vendas
GROUP BY "Payment"
ORDER BY quantidade_transacoes DESC;

-- Resultado: Ewallet 345 | Cash 344 | Credit card 311

-- 11. Faturamento por linha de produto
SELECT
    "Product line",
    SUM(CAST("Sales" AS NUMERIC)) AS faturamento
FROM raw_vendas
GROUP BY "Product line"
ORDER BY faturamento DESC;

-- Resultado:
-- Food and beverages: 56.144,844
-- Sports and travel: 55.122,8265
-- Electronic accessories: 54.337,5315
-- Fashion accessories: 54.305,895
-- Home and lifestyle: 53.861,913
-- Health and beauty: 49.193,739

-- 12. Avaliação média por linha de produto
SELECT
    "Product line",
    AVG(CAST("Rating" AS NUMERIC)) AS avaliacao_media
FROM raw_vendas
GROUP BY "Product line"
ORDER BY avaliacao_media DESC;

-- Resultado:
-- Food and beverages: 7,1132  <- Melhor avaliação média
-- Fashion accessories: 7,0292
-- Health and beauty: 7,0033
-- Electronic accessories: 6,9247
-- Sports and travel: 6,9163
-- Home and lifestyle: 6,8375

-- 13. Identificar a maior venda registrada
SELECT *
FROM raw_vendas
WHERE CAST("Sales" AS NUMERIC) = (
    SELECT MAX(CAST("Sales" AS NUMERIC))
    FROM raw_vendas
);

-- Resultado:
-- Invoice ID: 860-79-0874
-- Filial: Giza
-- Cidade: Naypyitaw
-- Maior venda: 1.042,65

-- 14. Filtrar vendas por intervalo de datas
SELECT *
FROM raw_vendas
WHERE TO_DATE("Date", 'MM/DD/YYYY')
      BETWEEN DATE '2019-01-01' AND DATE '2019-01-31';

-- 15. Verificar Invoice ID nulo ou vazio
SELECT *
FROM raw_vendas
WHERE "Invoice ID" IS NULL
   OR "Invoice ID" = '';

-- Resultado:
-- Nenhum Invoice ID nulo ou vazio encontrado.

-- 16. Verificar Invoice ID duplicado
SELECT
    "Invoice ID",
    COUNT(*) AS quantidade
FROM raw_vendas
GROUP BY "Invoice ID"
HAVING COUNT(*) > 1;

-- Resultado:
-- Nenhum Invoice ID duplicado encontrado.


-- 17. Calcular o valor médio geral das vendas
SELECT
    AVG(CAST("Sales" AS NUMERIC)) AS valor_medio_vendas
FROM raw_vendas;

-- Resultado: Valor médio geral das vendas 322,97