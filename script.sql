CREATE DATABASE ubots;

\c ubots;

CREATE TABLE filme (
    -- pk auto-incrementada
    id serial primary key,
    titulo text,
    sinopse text
);

INSERT INTO filme (titulo, sinopse) VALUES ('TITANIC', 'JACK E ROSE MORREM NO MAR');

CREATE TABLE avaliacao (
    id serial primary key,
    nota integer check (nota >= 1 and nota <= 5),
    -- fk
    filme_id integer references filme (id)
);

INSERT INTO avaliacao (nota, filme_id) VALUES (5, 1);
