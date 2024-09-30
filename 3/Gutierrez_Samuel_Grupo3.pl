% Algoritmos potencia

% Recursión Normal
normal(_, 0, 1) :- !.
normal(Base, Exponente, Resultado) :-
    Exponente > 0,
    NuevoExponente is Exponente - 1,
    normal(Base, NuevoExponente, Parcial),
    Resultado is Base * Parcial.
% ej: 2^8 => normal(2, 8, Resultado).

% Tail Recursion
tail(_, 0, Acumulador, Acumulador) :- !.
tail(Base, Exponente, Acumulador, Resultado) :-
    Exponente > 0,
    NuevoExponente is Exponente - 1,
    NuevoAcumulador is Acumulador * Base,
    tail(Base, NuevoExponente, NuevoAcumulador, Resultado).
% ej: 3^5 => tail(3, 5, 1, Resultado).

% Algoritmos Contar Elementos Repetidos

contar(_, [], 0).
contar(Elemento, [Elemento|Resto], Conteo) :-
    contar(Elemento, Resto, ConteoResto),
    Conteo is ConteoResto + 1.
contar(Elemento, [Cabeza|Resto], Conteo) :-
    Elemento \= Cabeza,
    contar(Elemento, Resto, Conteo).

remover(_, [], []).
remover(Elemento, [Elemento|Resto], Resultado) :-
    remover(Elemento, Resto, Resultado).
remover(Elemento, [Cabeza|Resto], [Cabeza|Resultado]) :-
    Elemento \= Cabeza,
    remover(Elemento, Resto, Resultado).

repetidos([], 0) :- !.
repetidos([Cabeza|Resto], ConteoFinal) :-
    contar(Cabeza, [Cabeza|Resto], Conteo),
    remover(Cabeza, Resto, NuevaLista),
    repetidos(NuevaLista, ConteoParcial),
    (Conteo > 1, ConteoFinal is ConteoParcial + 1 ; Conteo =< 1, ConteoFinal is ConteoParcial), !.

% ej: [16,5,3,1,5,3] => repetidos([16,5,3,1,5,3], Resultado).