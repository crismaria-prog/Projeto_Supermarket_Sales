CREATE TABLE raw_vendas (
    id_ingestao BIGSERIAL PRIMARY KEY,
    "Invoice ID" TEXT,
    "Branch" TEXT,
    "City" TEXT,
    "Customer type" TEXT,
    "Gender" TEXT,
    "Product line" TEXT,
    "Unit price" TEXT,
    "Quantity" TEXT,
    "Tax 5%" TEXT,
    "Sales" TEXT,
    "Date" TEXT,
    "Time" TEXT,
    "Payment" TEXT,
    "cogs" TEXT,
    "gross margin percentage" TEXT,
    "gross income" TEXT,
    "Rating" TEXT
);

CREATE TABLE vendas_tratadas (
    id_venda VARCHAR(50) PRIMARY KEY,
    filial VARCHAR(50) NOT NULL,
    cidade VARCHAR(100) NOT NULL,
    tipo_cliente VARCHAR(50),
    genero VARCHAR(20),
    linha_produto VARCHAR(150) NOT NULL,

    preco_unitario NUMERIC(10,2)
        CHECK (preco_unitario >= 0),

    quantidade INTEGER
        CHECK (quantidade > 0),

    imposto NUMERIC(12,4)
        CHECK (imposto >= 0),

    valor_total NUMERIC(12,4)
        CHECK (valor_total >= 0),

    data_venda DATE,
    hora_venda TIME,

    forma_pagamento VARCHAR(50) NOT NULL,

    custo_mercadoria NUMERIC(12,2)
        CHECK (custo_mercadoria >= 0),

    margem_percentual NUMERIC(10,6),

    receita_bruta NUMERIC(12,4)
        CHECK (receita_bruta >= 0),

    avaliacao NUMERIC(4,2)
        CHECK (avaliacao BETWEEN 0 AND 10),

    dia_semana VARCHAR(20),
    mes_venda INTEGER,
    ano_venda INTEGER,
    valor_sem_imposto NUMERIC(12,4)
);