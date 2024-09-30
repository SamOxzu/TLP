% Base de Conocimientos

% Hechos estudiantes (nombre, edad, usuario)
estudiante(pepe, 20, pepgomz).
estudiante(pepita, 22, pepherh).
estudiante(juan, 17, jusilcu).
estudiante(juan, 21, jupatno).

% Hechos sobre cursos (usuario, asignatura)
cursa(pepgomz, calculo).
cursa(pepgomz, etica).
cursa(pepherh, calculo).
cursa(jusilcu, etica).
cursa(jupatno, calculo).

% Hechos sobre notas (usuario, asignatura, nota)
nota(pepgomz, calculo, 2.7).
nota(pepgomz, etica, 3.8).
nota(pepherh, calculo, 3.9).
nota(jusilcu, etica, 4.3).
nota(jupatno, calculo, 4.8).

% Reglas

% Quienes van ganando cálculo (nota mayor o igual a 3.0)
gana_calculo(Estudiante) :-
    cursa(Estudiante, calculo),
    nota(Estudiante, calculo, Nota),
    Nota >= 3.0.

% Quienes van ganando ética (nota mayor o igual a 3.0)
gana_etica(Estudiante) :-
    cursa(Estudiante, etica),
    nota(Estudiante, etica, Nota),
    Nota >= 3.0.

% Estudiantes mayores de edad (mayores de 18 años)
mayor_de_edad(Estudiante) :-
    estudiante(_ , Edad, Estudiante),
    Edad >= 18.

% Estudiantes con notas mayores a 4.0
teso(Estudiante) :-
    nota(Estudiante, _, Nota),
    Nota > 4.0.

% Estudiantes con el mismo nombre (pero usuarios diferentes)
tocayos(Estudiante1, Estudiante2) :-
    Estudiante1 \== Estudiante2,
    estudiante(Nombre1, _, Estudiante1),
    estudiante(Nombre2, _, Estudiante2),
    Nombre1 = Nombre2,
    Estudiante1 @< Estudiante2.

% Consultas

% Nombres de todos los estudiantes
% estudiante(Estudiante, _, _).

% ¿Cuáles son los cursos que están cursando?
% Estudiante específico:
% cursa(*usuario*, Curso).
% Todos los estudiantes:
% cursa(Usuario, Curso).

% ¿Quiénes van ganando cálculo?
% gana_calculo(Estudiante).

% ¿Quiénes van ganando ética?
% gana_etica(Estudiante).

% ¿Cuáles estudiantes son mayores de edad?
% mayor_de_edad(Estudiante).

% ¿Cuáles estudiantes tienen notas mayores a 4.0?
% teso(Estudiante).

% ¿Cuáles estudiantes tienen el mismo nombre?
% tocayos(Estudiante1, Estudiante2).
