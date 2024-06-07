ostatni(L,[L]).
ostatni(M,[H|T]) :- ostatni(M,T).

przedostatni(BL,[BL,_]).
przedostatni(BL,[_|T]) :- przedostatni(BL,T).

bezostatniego([_], []).
bezostatniego([H|T], [H|L]) :- bezostatniego(T, L).

nakoniec(EL, [], [EL]).
nakoniec(EL, [H|T], [H|NT]) :- nakoniec(EL,T,NT).

zakazdym([],_,[]).
zakazdym([H|T], X, [H,X|NT]) :- zakazdym(T,X,NT).

codrugi([], []).
codrugi([_], []).
codrugi([_,E|T], [E|L]) :- codrugi(T, L).

wstaw_za([X|T], X, Y, [X,Y|T]).
wstaw_za([H|T], X, Y, [H|L]) :-  wstaw_za(T, X, Y, L).

lewoprawo(X, [X|T], [], T).
lewoprawo(X, [H|T], [H|LL], LP) :- lewoprawo(X, T, LL, LP).

wymiana(X, Y, [], []).
wymiana(X, Y, [X|T], [Y|E]) :- wymiana(X, Y, T, E).
wymiana(X, Y, [H|T], [H|E]) :- H \= X, wymiana(X, Y, T, E).

polacz([], []).
polacz([H|T], LP) :-append(H, T1, LP), polacz(T, T1).   
