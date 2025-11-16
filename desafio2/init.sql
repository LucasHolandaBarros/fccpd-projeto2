CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(50)
);

INSERT INTO clientes (nome, email) VALUES
('Lucas', 'lucas@email.com'),
('Maria', 'maria@email.com');