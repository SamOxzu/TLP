invertir(O, V) :- inv_tail(O, 0, V).
inv_tail(0, V, V).
inv_tail(O, A, V) :-
 X is O mod 10,
 U is O // 10,
 B is A * 10 + X,
 inv_tail(U, B, V).