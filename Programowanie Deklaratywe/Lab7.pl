sumuj([], 0).
sumuj([H|T], S) :- sumuj(T, SR), S is H + SR.
podzielniki(X, X, []) :- !.
podzielniki(N, D, [D|T]) :- D < N, 0 is mod(N, D), !, ND is D + 1, podzielniki(N, ND, T).
podzielniki(N, D, T) :- D < N, ND is D + 1, podzielniki(N, ND, T).
doskonala(N) :- podzielniki(N, 1, P), sumuj(P, W), W =:= N.

przekroj([], [], []) :- !.
przekroj(_, [], []) :- !.
przekroj([], _, []) :- !.
przekroj([X|T1], [X|T2], [X|T]) :- przekroj(T1, T2, T).
przekroj([H1|T1], [H2|T2], L) :- H1 < H2, przekroj(T1, [H2|T2], L).
przekroj([H1|T1], [H2|T2], L) :- H1 > H2, przekroj([H1|T1], T2, L).

glowyogony([], [], []).
glowyogony([[H|T]|O], [H|LG], [T|LO]) :- glowyogony(O, LG, LO).
slad([[X]], X).
slad(M, S) :- M = [H|T], glowyogony([H|T], [G|_], [_|LO]), slad(LO, NS), S is NS + G.

rozszerzaj([[P, K]], [P, K]).
rozszerzaj([[P, K]|T], [P, K]) :- rozszerzaj(T, [OP, OK]), P=<OP, K>=OK.
rozszerzaj([[P, K]|T], [OP, K]) :- rozszerzaj(T, [OP, OK]), P>OP, K>=OK.
rozszerzaj([[P, K]|T], [P, OK]) :- rozszerzaj(T, [OP, OK]), P=<OP, K<OK.
rozszerzaj([[P, K]|T], [OP, OK]) :- rozszerzaj(T, [OP, OK]), P>OP, K<OK.
ciagliczb(X, X, [X]) :- X > 0.
ciagliczb(M, N, [M|T]) :- M > 0, N > 0, M =< N, !, M1 is M + 1, ciagliczb(M1, N, T).

ciagliczb(X, X, [X]) :- X>0.
ciagliczb(M, N, [M|T]) :- M>0, N>0, M=<N, !, M1 is M+1, ciagliczb(M1, N, T).
liczpodziel(N, N, 0).
liczpodziel(N, D, C) :- D < N, mod(N,D) =:= 0, !, ND is D+1, liczpodziel(N, ND, S), C is S+1, !.
liczpodziel(N, D, C) :- D < N, ND is D+1, liczpodziel(N, ND, C), !.
antyp([], _).
antyp([H|T], LP) :- liczpodziel(H, 1, C), C < LP, antyp(T, LP), !.
antypierwsza(N) :- CN is N - 1, ciagliczb(1, CN, CL), liczpodziel(N, 1, LP), !, antyp(CL, LP).

rozmien(L, X, [X]) :- append(_, [X], L).
rozmien(L, N, R) :- append(_, [T], L), T < N, !, NN is N-T, rozmien(L, NN, OR), append(OR, [T], R).
rozmien(L, N, R) :- append(P, [T], L), T > N, !, rozmien(P, N, R).

wpolu([],_,[]).
wpolu([[X,Y]|T],[[X1,Y1],[X2,Y2]],[[X,Y]|LN]):-X1=<X,X=<X2,Y1=<Y,Y=<Y2,wpolu(T,[[X1,Y1],[X2,Y2]],LN).
wpolu([[X,Y]|T],[[X1,Y1],[X2,Y2]],LN):-X<X1,wpolu(T,[[X1,Y1],[X2,Y2]],LN).
wpolu([[X,Y]|T],[[X1,Y1],[X2,Y2]],LN):-X>X2,wpolu(T,[[X1,Y1],[X2,Y2]],LN).
wpolu([[X,Y]|T],[[X1,Y1],[X2,Y2]],LN):-Y<Y1,wpolu(T,[[X1,Y1],[X2,Y2]],LN).
wpolu([[X,Y]|T],[[X1,Y1],[X2,Y2]],LN):-Y>Y2,wpolu(T,[[X1,Y1],[X2,Y2]],LN).

minX([[X,_]], X).
minX([[H,_]|T], H) :- minX(T, X), H < X.
minX([[H,_]|T], X) :- minX(T, X), H >= X.
maxX([[X,_]], X).
maxX([[H,_]|T], H) :- maxX(T, X), H > X.
maxX([[H,_]|T], X) :- maxX(T, X), H =< X.
minY([[_,X]], X).
minY([[_,H]|T], H) :- minY(T, X), H < X.
minY([[_,H]|T], X) :- minY(T, X), H >= X.
maxY([[_,X]], X).
maxY([[_,H]|T], H) :- maxY(T, X), H > X.
maxY([[_,H]|T], X) :- maxY(T, X), H =< X.
minpole(L, [[MinX,MinY],[MaxX, MaxY]]) :- minX(L, MinX), minY(L, MinY), maxX(L, MaxX), maxY(L, MaxY).

zamien_g([], []).
zamien_g([X],[X]).
zamien_g([X,Y|Z], [X|W]) :- Y >= X, zamien_g([Y|Z], W).
zamien_g([X,Y|Z], [Y|W]) :- Y < X, zamien_g([X|Z], W).
zamien_d([], []).
zamien_d([X], [X]).
zamien_d([X,Y|Z], [X|W]) :- Y =< X, zamien_d([Y|Z],W).
zamien_d([X,Y|Z], [Y|W]) :- Y > X, zamien_d([X|Z],W).
odwracaj([], []).
odwracaj([X|Y],Z) :- odwracaj(Y,W), append(W,[X],Z).
koktajl([], []).
koktajl([X], [X]).
koktajl(X,Y) :-zamien_g(X,Z), odwracaj(Z,[W|V]), zamien_d(V,U), odwracaj(U,[T|S]), koktajl(S,R), append([T|R],[W],Y).

ciagFib(N, A, B, [A, B]) :- C is A + B, N < C, !.
ciagFib(N, A, B, [A|T]) :- C is A + B, N >= C, ciagFib(N, B, C, T).
rozklad([X|_], X, [X]) :- !.
rozklad([_|T], N, R) :- rozklad(T, N, R).
rozklad(L, N, R) :- append(_, [T], L), T < N, M is N - T, rozklad(L, M, P), append(P, [T], R).
rozklad(L, N, R) :- append(P, [T], L), T > N, rozklad(P, N, R).
rozklad_fib(N, R) :- ciagFib(N, 0, 1, F), rozklad(F, N, R).
