CREATE TABLE IF NOT EXISTS produtos (
    id SERIAL PRIMARY KEY,
    nome TEXT
);

INSERT INTO produtos (nome) VALUES ('banana'), ('maçã'), ('laranja');
