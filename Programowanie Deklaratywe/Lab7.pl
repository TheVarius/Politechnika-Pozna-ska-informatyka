najwiekszy([X],X).
najwiekszy([H|T],H) :- najwiekszy(T,Y), H > Y.
najwiekszy([H|T],Y) :- najwiekszy(T,Y), H =< Y.

liniowa([_,_]).
liniowa([A,B,C|T]) :- A-B =:= B-C, liniowa([B,C|T]).

rozbij([], [], []).
rozbij(L1, [N|L2], [P|L]) :- N > 0, append(P, R, L1), length(P, N), rozbij(R, L2, L).

przynaleznosc([], [_, _], [], []).
przynaleznosc([H|T], [L, P], [H|LW], LZ) :- H >= L, H =< P, !, przynaleznosc(T, [L, P], LW, LZ).
przynaleznosc([H|T], [L, P], LW, [H|LZ]) :- H < L, przynaleznosc(T, [L, P], LW, LZ).
przynaleznosc([H|T], [L, P], LW, [H|LZ]) :- H > P, przynaleznosc(T, [L, P], LW, LZ).

decnabin(0, [0]) :- !.
decnabin(1, [1]) :- !.
decnabin(N, B) :- N > 0, N1 is N div 2, R is N mod 2, decnabin(N1, B1), append(B1, [R], B).

rozdziel([], _, [], []).
rozdziel([Y], X, [Y], []) :- Y < X, !.
rozdziel([Y], _, [], [Y]).
rozdziel([H|T], X, [H|L1], L2) :- H < X, !, rozdziel(T, X, L1, L2).
rozdziel([H|T], X, L1, [H|L2]) :- rozdziel(T, X, L1, L2).

szybkisort([], []).
szybkisort([P|T], L) :- rozdziel(T, P, L1, L2), szybkisort(L1, S1), szybkisort(L2, S2), append(S1, [P|S2], L).

doposort([], X, [X]).
doposort([H|T], X, [X,H|T]) :- X =< H, !.
doposort([H|T], X, [H|L2]) :- X > H, doposort(T, X, L2).
wstawsort([], []).
wstawsort([H|T], S) :- wstawsort(T, S1), doposort(S1, H, S).

unikalne([], []).
unikalne([X], [X]).
unikalne([H|T], Y) :- unikalne(T, Y), member(H,Y), !.
unikalne([H|T], [H|Y]) :- unikalne(T,Y), not(member(H,Y)).

najblizszy(_, [X], X).
najblizszy(X, [H|T], Y) :- najblizszy(X,T,Y), abs(H-X) > abs(Y-X), !.
najblizszy(X, [H|T], H) :- najblizszy(X,T,Y), abs(H-X) =< abs(Y-X), !.

ciagliczb(X, X, [X]) :- X > 0. 
ciagliczb(M, N, [M|T]) :- M > 0, N > 0, M =< N, M1 is M + 1, ciagliczb(M1, N, T).

odsiewaj(_, [], []). 
odsiewaj(X, [H|T], [H|R]) :- 0 =\= H mod X, odsiewaj(X, T, R). 
odsiewaj(X, [H|T], R) :- 0 =:= H mod X, odsiewaj(X, T, R).

sito([], []). 
sito([H|T], [H|P]) :- odsiewaj(H, T, R), sito(R, P).

eratostenes(N, L) :- ciagliczb(2, N, A), sito(A, L).
