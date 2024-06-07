klonuj([],[]).
klonuj([H|T],[[H,H]|L]) :- klonuj(T,L).

srodek([A],A).
srodek([_|T], X) :- append(L,[_],T), srodek(L,X).

polowki([],[],[]).
polowki([H|T],LL,LP) :-append(L,[E],T), polowki(L,LL1,LP1), append([H],LL1,LL),append(LP1,[E],LP).

sumuj([],0).
sumuj([H|T], S) :- sumuj(T, ST), S is H + ST.

ile_wiekszych([], _, 0).
ile_wiekszych([H|T], X, N) :- H > X, ile_wiekszych(T, X, N1), N is N1 + 1.
ile_wiekszych([H|T], X, N) :- H =< X,  ile_wiekszych(T, X, N). 

plus_minus([], 0).
plus_minus([+|T], X) :- plus_minus(T, X1), X is X1 + 1.
plus_minus([-|T], X) :- plus_minus(T, X1), X is X1 - 1.

wstawiaj([], X, 1, [X]).
wstawiaj([H | T], X, 1, [X, H | T]).
wstawiaj([H | T], X, N, [H | NT]) :- N > 1, N1 is N - 1, wstawiaj(T, X, N1, NT).

usuwaj([_|T], 1, T).
usuwaj([_|T], X, NT) :- X1 is X-1, usuwaj(T, X1, NT).

rozdziel([], _, [], []).
rozdziel([H|T], X, [H|L1], L2) :- H < X, rozdziel(T, X, L1, L2).
rozdziel([H|T], X, L1, [H|L2]) :- H >= X, rozdziel(T, X, L1, L2).

powiel([], [], []).
powiel([H|T], [0|LT], L) :- powiel(T, LT, L).
powiel([H|T], [X|LT], [H|NT]) :- X > 0, X1 is X - 1, powiel([H|T], [X1|LT], NT).
