# python-iterations
Iterations ... en Python!

## Instructions

Vous trouverez les sujets pour chaque fichier en suivant les liens:
- [taxes.py](https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w4/w4-s3-x2-taxes)
- [comprehensions.py](https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w5/w5-s3-x1-comprehensions)
- [vigenere.py](https://nbhosting.inria.fr/auditor/notebook/exos-mooc:exos/w5/w5-s3-x2-vigenere)
- [digits.py](https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python)

Copiez votre code dans les différentes fonctions des fichiers.

Attention, il ne faut pas changer le nom des fonctions, ni le nombre d'arguments.

Exécutez les tests en local (cf ci-dessous).

Quand le résultat est satisfaisant, git add, git commit, git push:

```shell
$ git add vigenere.py
$ git commit --message "code de cesar"
$ git push
```

## Exécuter les tests localement

```shell
$ python grader.py
```

Il est courant de se tromper et de faire des boucles infinies dans son code. Dans ce cas,
les tests n'arriveront jamais "au bout". Appuyez sur `Ctrl + C` pour interrompre le grader.
