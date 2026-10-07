-- Active: 1788283801116@@127.0.0.1@5432@catalogo_filmes
SELECT * FROM usuarios;
SELECT * FROM filmes;
SELECT titulo, genero, nota
FROM filmes
WHERE nota > 8;
SELECT titulo, ano_lancamento, nota, genero
FROM filmes
WHERE genero = 'Terror';
SELECT titulo, ano_lancamento, genero
FROM filmes
WHERE ano_lancamento > '2000-01-01';
SELECT titulo, genero, nota
FROM filmes
WHERE usuario_id = 1;