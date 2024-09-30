remover(_, [], []).
remover(E, [T|C], S) :- E = T, remover(E, C, S).
remover(E, [T|C], [T|S]) :- E \= T,remover(E, C, S).