hijo(sebas,estefa). hijo(sebas,mario). 

hijo(juanita,estefa). hijo(juanita,mario). 

hijo(estefa,carlos). hijo(estefa,claudia). 

hijo(lola, mario). hijo(rodrigo, consuelo).

hijo(rodrigo,sebas). hijo(marta, juanita).

hijo(freddy, juanita). hijo(susana, juanita).

hijo(marta, luis). hijo(freddy, luis).

hijo(susana, luis).

hombre(sebas). hombre(mario). hombre(carlos). hombre(rodrigo). hombre(freddy). 

hombre(luis).

mujer(estefa). mujer(juanita). mujer(claudia). mujer(marta). mujer(susana).

mujer(lola). mujer(consuelo).

padre(P,X) :- hijo(X,P), hombre(P). 

madre(M,X) :- hijo(X,M), mujer(M). 

sexo_opuesto(X,Y) :- hombre(X), mujer(Y). 

sexo_opuesto(Y,X) :- hombre(X), mujer(Y). 

abuelo(X,Z) :- padre(X,Y), hijo(Z,Y). 

abuela(Y,Z) :- madre(Y,R), hijo(Z,R). 

hermanos(X, Y) :- hijo(X, Z), hijo(Y, Z), X\=Y.

/* REGLAS TAREA 1 */

tio(T,X) :- hombre(T), hermanos(T,P), hijo(X,P).

sobrino(X,T) :- hermanos(T,P), hijo(X,P).

primos(X,P) :- hijo(P,T), sobrino(X,T).

bisabuela(B,N) :- mujer(M), hijo(A,B), abuela(A,N).