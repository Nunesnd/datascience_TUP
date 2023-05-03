create database desafio_21_dias;

use desafio_21_dias;

create table pessoas (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(150) NOT NULL,
    idade INT NOT NULL,
    cidade VARCHAR(250) NOT NULL
    PRIMARY KEY (id)
);