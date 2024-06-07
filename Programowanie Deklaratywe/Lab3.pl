next(świnoujście,kołobrzeg).
next(świnoujście, szczecin).
next(kołobrzeg,ustka).
next(ustka, gdańsk).
next(gdańsk,toruń).
next(gdańsk,olsztyn).
next(olsztyn,toruń).
next(olsztyn,białystok).
next(szczecin,bydgoszcz).
next(szczecin, gorzów-wlkp).
next(bydgoszcz,toruń).
next(bydgoszcz,poznań).
next(poznań,toruń).
next(gorzów-wlkp,poznań).
next(gorzów-wlkp,zielona-góra).
next(zielona-góra,poznań).
next(zielona-góra,wrocław).
next(toruń,łódź).
next(toruń,warszawa).
next(białystok, warszawa).
next(białystok,lublin).
next(poznań,łódź).
next(warszawa,radom).
next(warszawa,łódź).
next(radom,lublin).
next(radom,kielce).
next(wrocław,łódź).
next(łódź,radom).
next(łódź,częstochowa).
next(częstochowa,kielce).
next(częstochowa,katowice).
next(katowice,kraków).
next(kielce,kraków).
next(kielce,rzeszów).
next(lublin,kielce).
next(lublin,rzeszów).
next(kraków,rzeszów).

połączenie(A,B) :- next(A,B).
połączenie(A,B) :- next(A,C), połączenie(C,B).

zjazd(A,B,A) :- next(A,B).
zjazd(A,B,C) :- next(A,X), zjazd(X,B,C).

trasa(A,B,obok(A,B)) :- next(A,B).
trasa(A,B,obok(A,W)) :- next(A,P), trasa(P,B,W).

trasa2(A,B,obok(A,B)) :- next(A,B).
trasa2(A,B,obok(W,B)):-next(P,B),trasa2(A,P,W).

trasa3(A, B, [A, B]) :- next(A, B).
trasa3(A, B, [A | P]) :- next(A, W), trasa3(W, B, P).
