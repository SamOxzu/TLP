digito(1).
digito(2).
digito(3).
digito(4).
digito(5).
digito(6).
digito(7).
digito(8).
digito(9).
cuadrado_magico(P11, P12, P13, P21, P22, P23, P31, P32, P33) :-
 digito(P11), digito(P12), digito(P13),
 digito(P21), digito(P22), digito(P23),
 digito(P31), digito(P32), digito(P33),
 P11 \= P12, P11 \= P13, P11 \= P21, P11 \= P22, P11 \= P23, P11 \= P31, P11 \= P32, 
P11 \= P33,
 P12 \= P13, P12 \= P21, P12 \= P22, P12 \= P23, P12 \= P31, P12 \= P32, P12 \= P33,
 P13 \= P21, P13 \= P22, P13 \= P23, P13 \= P31, P13 \= P32, P13 \= P33,
 P21 \= P22, P21 \= P23, P21 \= P31, P21 \= P32, P21 \= P33,
 P22 \= P23, P22 \= P31, P22 \= P32, P22 \= P33,
 P23 \= P31, P23 \= P32, P23 \= P33,
 P31 \= P32, P31 \= P33,
 P32 \= P33,
 (P11 + P21 + P31) =:= (P11 + P12 + P13),
 (P11 + P12 + P13) =:= (P13 + P23 + P33),
 (P13 + P23 + P33) =:= (P31 + P32 + P33),
 (P31 + P32 + P33) =:= (P12 + P22 + P32),
 (P12 + P22 + P32) =:= (P21 + P22 + P23),
 (P21 + P22 + P23) =:= (P11 + P22 + P33),
 (P11 + P22 + P33) =:= (P31 + P22 + P13).