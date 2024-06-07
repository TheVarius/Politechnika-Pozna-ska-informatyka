kobieta(maria).
kobieta(ewa).
kobieta(joanna).
kobieta(anna).
kobieta(agata).
kobieta(agnieszka).
kobieta(beata).
kobieta(iwona).

mężczyzna(piotr).
mężczyzna(adam).
mężczyzna(marek).
mężczyzna(robert).
mężczyzna(jan).
mężczyzna(krzysztof).
mężczyzna(radek).
mężczyzna(darek).
mężczyzna(tomek).
mężczyzna(jacek).

rodzic(maria,marek).
rodzic(maria,agata).
rodzic(maria,jan).
rodzic(piotr,marek).
rodzic(piotr,agata).
rodzic(piotr,jan).
rodzic(adam,joanna).
rodzic(adam,anna).
rodzic(adam,krzysztof).
rodzic(ewa,joanna).
rodzic(ewa,anna).
rodzic(ewa,krzysztof).
rodzic(robert,radek).
rodzic(robert,beata).
rodzic(agata,radek).
rodzic(agata,beata).
rodzic(jan,darek).
rodzic(jan,tomek).
rodzic(anna,darek).
rodzic(anna,tomek).
rodzic(krzysztof,jacek).
rodzic(krzysztof,iwona).
rodzic(agnieszka,jacek).
rodzic(agnieszka,iwona).
małżeństwo(maria,piotr).
małżeństwo(adam,ewa).
małżeństwo(robert,agata).
małżeństwo(jan,anna).
małżeństwo(krzysztof,agnieszka).

matka(X,Y) :- kobieta(X), rodzic(X,Y).
mąż(X,Y) :- mężczyzna(X), małżeństwo(X,Y).
mąż(Y,X) :- mężczyzna(Y), małżeństwo(X,Y).
ojciec(X,Y) :- mężczyzna(X), rodzic(X,Y).
rodzeństwo(X,Y) :- rodzic(Z,X), rodzic(Z,Y), X\=Y.
siostra(X,Y) :- kobieta(X), rodzic(Z,X), rodzic(Z,Y), X\=Y.
brat(X,Y) :- mężczyzna(X), rodzic(Z,X), rodzic(Z,Y), X\=Y.
babcia(X,Y) :- kobieta(X), rodzic(X,Z), rodzic(Z,Y).
dziadek(X,Y) :- mężczyzna(X), rodzic(X,Z), rodzic(Z,Y).
wuj(X,Y) :- mężczyzna(X), rodzic(Z,Y), kobieta(Z), brat(X,Z).
stryj(X,Y) :- mężczyzna(X), rodzic(Z,Y), mężczyzna(Z), brat(X,Z), X\=Z.
kuzyn(X,Y) :- rodzeństwo(Z,U), rodzic(U,Y), rodzic(Z,X), mężczyzna(X).
teściowa(X,Y) :- mąż(Y,Z), matka(X,Z).
szwagier(X,Y) :- mąż(Y,Z), brat(X,Z).
szwagier(X,Y) :- mąż(X,Z), siostra(Z,Y).
