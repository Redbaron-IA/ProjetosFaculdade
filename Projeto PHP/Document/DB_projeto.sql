CREATE DATABASE DB_projeto;
USE DB_projeto;

CREATE TABLE autores (
idAutor INT PRIMARY KEY AUTO_INCREMENT,
autores CHAR(60)
);

CREATE TABLE livros (
registro INT PRIMARY KEY AUTO_INCREMENT, 
titulo CHAR(60), 
editora CHAR(60),
edicao CHAR(60),
fichaCatalogo TINYTEXT, 
idAutor INT(4)
);

CREATE TABLE funcionarios (
matriculaFun INT PRIMARY KEY AUTO_INCREMENT,
nome CHAR(60),
email CHAR(60),
telefone CHAR(12), 
login CHAR(15),
senha CHAR(10)
);

CREATE TABLE usuarios (
matriculaUs INT PRIMARY KEY AUTO_INCREMENT,
nome CHAR(60),
email CHAR(60),
telefone CHAR(12)
);

CREATE TABLE emprestimos (
id_emprestimo INT PRIMARY KEY AUTO_INCREMENT,
matriculaFun INT(6),
matriculaUs INT(6),
registro INT(6),
dataEmprestimo DATE, 
dataDevolucao DATE
);

ALTER TABLE emprestimos ADD CONSTRAINT fk_funcionario FOREIGN KEY (matriculaFun) REFERENCES funcionarios (matriculaFun);
ALTER TABLE emprestimos ADD CONSTRAINT fk_usuario FOREIGN KEY (matriculaUs) REFERENCES usuarios (matriculaUs);
ALTER TABLE emprestimos ADD CONSTRAINT fk_livro FOREIGN KEY (registro) REFERENCES livros (registro);
ALTER TABLE livros ADD CONSTRAINT fk_autor FOREIGN KEY (idAutor) REFERENCES autores (idAutor);