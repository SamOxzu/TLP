% Paco es hermano del estudiante de Sistemas
estudiante(paco, Carrera, _) :- Carrera \= sistemas.
% Al de Industrial le gusta el fútbol
estudiante(_, industrial, futbol).
% Paco no estudia Química
estudiante(paco, Carrera, _) :- Carrera \= quimica.
% Hugo le regaló un café al nadador para que termine
% su taller de programación orientada a objetos
estudiante(hugo, _, Deporte) :- Deporte \= natacion.
% ¿Quién practica tenis?
practica_tenis(Estudiante) :-
 estudiante(Estudiante, _, tenis).