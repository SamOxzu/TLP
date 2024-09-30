potencia(_, 0, 1):-!.
potencia(Bas, Exp, N) :- E is Exp -1, potencia(Bas, E, A), N is Bas*A.