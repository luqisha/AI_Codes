/* Prolog code for finding brother/sister/uncle/aunt of a person in a given KB of kinship domain */

parent('Hasib' , 'Rakib').
parent('Rakib' , 'Sohel').
parent('Rakib' , 'Rebeka').
parent('Rashid' , 'Hasib').
parent('Rakib', 'Asif').
parent('Rakib', 'Saber').
parent('Rabeya', 'Asif').
parent('Rabeya', 'Sohel').
parent('Hasib', 'Rakhi').
parent('Samir', 'Rabeya').
parent('Samir', 'Akib').
parent('Samir', 'Tanny').

male('Hasib').
male('Rakib').
male('Sohel').
male('Rashid').
male('Ashiq').
male('Asif').
male('Samir').
male('Akib').
male('Saber').

female('Rebeka').
female('Rabeya').
female('Rakhi').
female('Tanny').

brother(X, Z) :- parent(P, X), parent(P, Z), male(Z), not(X = Z).
findBrother :- write('Name: '), read(X), nl, write('Brother/s of '), print(X), write(': '), nl,
    brother(X, Z), write(Z), tab(4), fail.

sister(X, Z) :-  parent(P, X), parent(P, Z), female(Z), not(X = Z).
findSister :- write('Name: '), read(X), nl, write('Sister/s of '), print(X), write(': '), nl,
    sister(X, Z), write(Z), tab(4), fail.

uncle(X, Z) :- parent(P, X), parent(G, P), parent(G, Z), male(Z), not(Z = P).
findUncle :- write('Name: '), read(X), nl, write('Uncle/s of '), print(X), write(': '), nl,
    uncle(X, Z), write(Z), tab(4), fail.

aunt(X, Z) :- parent(P, X), parent(G, P), parent(G, Z), female(Z), not(Z = P).
findAunt :- write('Name: '), read(X), nl, write('Aunt/s of '), print(X), write(': '), nl,
    aunt(X, Z), write(Z), tab(4), fail.




