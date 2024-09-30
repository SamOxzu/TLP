contar([], 0):-!.
contar([_|C], X):- contar(C, A), X is A+1.