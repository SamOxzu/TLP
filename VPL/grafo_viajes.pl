% VIAJES
% Origen Medellín
viaje(medellin, avion, cartagena).
viaje(medellin, avion, usa).
viaje(medellin, helicoptero, habana).
% Origen Cartagena
viaje(cartagena, avion, medellin).
viaje(cartagena, avion, usa).
viaje(cartagena, crucero, portugal).
viaje(cartagena, lancha, islas).
% Origen Islas
viaje(islas, lancha, cartagena).
% Origen Habana
viaje(habana, helicoptero, medellin).
viaje(habana, lancha, usa).
% Origen USA
viaje(usa, avion, medellin).
viaje(usa, avion, cartagena).
viaje(usa, avion, portugal).
viaje(usa, lancha, habana).
% Origen Portugal
viaje(portugal, avion, usa).
viaje(portugal, crucero, cartagena).
% Medios
valor(avion, 200000).
valor(helicoptero, 150000).
valor(lancha, 100000).
valor(crucero, 300000).

% CONSULTA
% Caso Base
consultar(N, N, _, _, _, _) :- !.
% Caso Adyacente
consultar(Origen, Destino, [Origen|Destino], Ptotal, [Pxtrayecto], [Transp]) :-
 viaje(Origen, Transp, Destino),
 valor(Transp, Ptotal),
 valor(Transp, Pxtrayecto).
% Caso no Adyacente
consultar(Origen, Destino, [Origen|Trayecto], Ptotal, [Pxtrayecto|Resto], 
[Trans|Transp]) :-
 viaje(Origen, Trans, Aux),
 valor(Trans, Pxtrayecto),
 consultar(Aux, Destino, Trayecto, Cost, Resto, Transp),
 Ptotal is Pxtrayecto + Cost.

consultar(medellin, portugal, Pasos, PrecioTotal
, PrecioPorTrayecto, Medios).