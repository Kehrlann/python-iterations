# python-iterations

Iterations ... en Python!


Les fonctions... en Python!

Vous allez faire 3 exercices. Pour le rendu, remplissez **uniquement les fonctions** dans les fichiers désignés, veillez bien à n'ajouter aucun autre code dans ces fichiers. Évaluez votre note en local de temps en temps (cf ci-dessous).

Pendant que vous préparez vos exercices, pouvez tester vos fonctions en utilisant la construction
`if __name__ == "__main__":`


```python
def toto(un, deux, trois):
  # votre code
  # ...

if __name__ == "__main__":
  resultat = toto("un", 2, three)
  print(resultat)
```

## Rendre votre travail

Quand le résultat pour un des exercices est satisfaisant, git add, git commit, git push:

```shell
$ git add vigenere.py
$ git commit --message "code de cesar"
$ git push
```

Rendus **obligatoires**:

- `taxes`
- `comprehensions`
- `vigenere`: le code de César

Rendus facultatifs:

- `vigenere`: le code de Vigénère
- `digits`

## Évaluer votre note en local

Vous pouvez évaluer votre note en local, avec:

```shell
$ python grader.py
```

Si les tests ne finissent jamais, appuyez sur `Ctrl + C` pour interrompre.

## Exercice - `taxes`

On se propose d'écrire une fonction `taxes` qui calcule le montant de l'impôt sur le revenu au Royaume-Uni.

Le barème est [publié ici par le gouvernement anglais](https://www.gov.uk/income-tax-rates), voici les données de 2020 qui sont utilisées pour l'exercice :

| Tranche             | Revenu imposable    | Taux  |
|--------------------:|--------------------:|------:|
| Non imposable       | jusque £12.500      | 0%    |
| Taux de base        | £12.501 à £50.000   | 20%   |
| Taux élevé          | £50.001 à £150.000  | 40%   |
| Taux supplémentaire | au delà de £150.000	| 45%   |

Donc naturellement il s'agit d'écrire une fonction qui prend en argument le revenu imposable, et retourne le montant de l'impôt, **arrondi à l'entier inférieur**.

Quelques exemples:

```python
>>> taxes(0)
0
>>> taxes(50000)
7500
>>> taxes(12500)
0
```

**Indices**

* évidemment on parle ici d'une fonction continue ;
* aussi en termes de programmation, je vous encourage à séparer la définition des tranches de la fonction en elle-même.

## Exercice - `comprehensions`

### Basique - `aplatir`

Il vous est demandé d'écrire une fonction `aplatir` qui prend *un unique* argument `l_conteneurs` qui est une liste (ou plus généralement un itérable) de conteneurs (ou plus généralement d'itérables), et qui retourne la liste de tous les éléments de tous les conteneurs.

```python
>>> aplatir([])
[]
>>> aplatir([(1,)])
[1]
>>> aplatir(([1],))
[1]
>>> aplatir([(0, 6, 2), [1, ('a', 4), 5]])
[ 0, 6, 2, 1, ('a', 4), 5]
>>> aplatir(([1, [2, 3]], ('a', 'b', 'c')))
[ 1, [2, 3], 'a', 'b', 'c']
>>> aplatir(([1, 6], ('c', 'b'), [2, 3]))
[ 1, 6, 'c', 'b', 2, 3]
>>> aplatir(((1, [2, 3]), [], 'a', ['b', 'c']))
[ 1, [2, 3], 'a', 'b', 'c']
```


### Intermédiaire - `alternat`

À présent, on passe en argument deux conteneurs (deux itérables) `c1` et `c2` de même taille à la fonction `alternat`, qui doit construire une liste contenant les éléments pris alternativement dans `c1` et dans `c2`.

```python
>>> alternat((1, 2), ('a', 'b'))
[1, 'a', 2, 'b']
>>> alternat((1, 2, 3), ('a', 'b', 'c'))
[ 1, 'a', 2, 'b', 3, 'c']
```

**Indice** pour cet exercice il peut être pertinent de recourir à la fonction *built-in* `zip`.


### Intermédiaire - `intersect`

On se donne deux ensembles A et B de tuples de la forme

```python
(entier, valeur)
```

On vous demande d'écrire une fonction `intersect` qui retourne l'ensemble des objets `valeur` associés (dans A ou dans B) à un entier qui soit présent dans (un tuple de) A *et* dans (un tuple de) B.

```python
>>> intersect(
  { (8, 'huit'), (10, 'dixA'), (12, 'douze')},
  { (5, 'cinq'), (10, 'dixB'), (15, 'quinze')})
{'dixB', 'dixA'}
>>> intersect(
  { (1, 'unA'), (2, 'deux'), (3, 'troisA')},
  { (1, 'unB'), (2, 'deux'), (4, 'quatreB')})
{'unA', 'deux', 'unB'}
```

## Exercice - `vigenere`

Le [code ou chiffre de Vigénère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re) est une méthode de chiffrement très rustique, qui est une version un peu améliorée du [chiffre de César](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage).

Les deux méthodes fonctionnent par simple décalage dans l'alphabet modulo 26.

*Je précise tout de suite que les conventions que nous avons adoptées dans cet exercice sont légèrement différentes de celles décrites dans les deux pages wikipédia citées ci-dessus.*


Dans le chiffre de **César**, on se donne une **clé** constituée d'**un seul caractère**, disons par exemple `C` (la 3-ième lettre de l'alphabet), et avec cette clé on chiffre l'alphabet par un décalage de 3, ce qui donne :

```
clé     : C    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC
```

ou avec d'autres clés

```
clé     : L
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : MNOPQRSTUVWXYZABCDEFGHIJKL
```

```
clé     : E    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : FGHIJKLMNOPQRSTUVWXYZABCDE
```

La méthode de **Vigenère** consiste à choisir cette fois pour **clé** un **mot**, qui est utilisé de manière répétitive. 

Ainsi par exemple si je choisis la clé `CLE`, on va chiffrer un message en appliquant la méthode de César

* avec la clé 'C' sur le 1-er caractère, 
* avec la clé 'L' sur le 2-ème caractère, 
* avec la clé 'E' sur le 3-ème caractère, 
* avec la clé 'C' sur le 4-ème caractère, 
* avec la clé 'L' sur le 5-ème caractère, 
* ...

Le but de cet exercice est d'écrire une fonction qui implémente la méthode de Vigenère pour, à partir d'une clé **connue**, coder ou décoder des messages.


### Première partie : le code de César

Dans un premier temps on se propose d'implémenter le code de César ; pour rester simple, nous allons nous limiter à ne chiffrer que **les caractères alphabétiques** dans la plage des caractères ASCII, c'est-à-dire sans accent, cédille ou autre.

Je rappelle par ailleurs l'existence en Python de deux fonctions qui peuvent être très utiles dans ce contexte :

* `ord()` qui projette les caractères vers les entiers (codepoints)
* et `chr()` qui réalise l'opération inverse.

```python
>>> ord('a')
97
>>> chr(97)
'a'
```

Une fois qu'on a dit ça, il est intéressant de constater que les caractères minuscules et majuscules auxquels nous nous intéressons sont, fort heureusement, contigus dans l'espace des codepoints.

```python
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.ascii_lowercase
'abcdefghijklmnopqrstuvwxyz'
```

On peut trouver les correspondances avec une boucle for:

```python
COLUMNS = 7
for index, char in enumerate(string.ascii_uppercase, 1):
    print(f"{char}→{ord(char):3d} ", end="")
    if index % COLUMNS == 0:
        print()    
```

Et l'inverse:

```python
COLUMNS = 7
for index, char in enumerate(string.ascii_lowercase, 1):
    print(f"{char}→{ord(char):3d} ", end="")
    if index % COLUMNS == 0:
        print()    
```

Forts de ces observations, vous devez pouvoir à présent écrire une première fonction qui implémente le décalage de César. 

Comme par ailleurs les opérations d'encodage et de décodage sont symétriques l'une de l'autre, on choisit pour éviter d'avoir à dupliquer du code, d'écrire une fonction dont la signature est :

```python
def cesar(clear, key, encode=True):
    # retourne un caractère
```


La fonction en question doit :

* laisser le texte tel quel si ce n'est pas un caractère alphabétique ASCII,
* accepter une clé qui peut être minuscule ou majuscule ; dit autrement, deux clés qui valent 'C' et 'c' produisent toutes les deux le même résultat,
* retourner une majuscule si le texte clair est en majuscule et une minuscule si le texte en clair est une minuscule.

Voici ce que cela donnerait sur quelques exemples :

```python
>>> cesar('=', 'C')
'='
>>> cesar('A', 'C')
'D'
>>> cesar('a', 'C')
'd'
>>> cesar('A', 'c')
'D'
>>> cesar('D', 'C', encode=False)
'A'
>>> cesar('A', 'L')
'M'
```

### Deuxième partie : le code de Vigenère

Cette première partie étant acquise, nous pouvons passer à l'amélioration de Vigenère, qui comme on l'a vu dans l'introduction consiste à prendre un mot dont on utilise les lettres successivement, et en boucle, comme clé pour la méthode de César.

Donc pour calculer le chiffrement de `ce message` avec la clé `cle`, on va se souvenir que:

```
clé     : C    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC
```

```
clé     : L
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : MNOPQRSTUVWXYZABCDEFGHIJKL
```

```
clé     : E    
clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
chiffré : FGHIJKLMNOPQRSTUVWXYZABCDE
```
et du coup faire:

```
cesar('c', 'c') → 'f'
cesar('e', 'l') → 'q'
cesar(' ', 'e') → ' '
cesar('m', 'c') → 'p'
cesar('e', 'l') → 'q'
cesar('s', 'e') → 'x'
cesar('s', 'c') → 'v'
cesar('a', 'l') → 'm'
cesar('g', 'e') → 'l'
cesar('e', 'c') → 'h'
```

Voyons cet exemple sous forme de code :

```python
>>> vigenere( 'ce message', 'cle')
'fq pqxvmlh'
>>> vigenere( 'fq pqxvmlh', 'CLE', False)
'ce message'
```

**Indices**

* Bien entendu vous êtes invités à utiliser la fonction `cesar` pour implémenter `vigenere`.

* Par ailleurs, pour cet exercice je vous recommande d'aller voir ou revoir le module `itertools` qui contient des outils qui sont exactement adaptés à ce traitement.  
  C'est-à-dire, pour être encore plus explicite, qu'il est possible d'écrire cette fonction sans recourir à aucun indice entier sur le texte ni sur la clé.


## Exercice - `digits`

Voir l'énoncé [sur Codewars](https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python).
