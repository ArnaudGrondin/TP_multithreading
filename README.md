# TP multithreading
## Arnaud grondin

Le but du tp est de comparer les différentes façons d'éxecuter des processus en comparant leur temps de calcul

## la tache :
la tache est défini dans le fichier source tache.py
Le but de la tache est de résoudre une équation du type X = A.B

### Tester l'execution :

Dans trois terminaux taper les commandes :
``` bash

$ uv run python manager.py
$ uv run python minion.py
$ uv run python boss.py

```

### Resultat execution tache  en python (10 taches de taille 1000)
###
 (fenêtre boss.py)
```bash
0.12012323400085734
0.33648354900105915
0.028514207999251084
0.025920832000338123
0.030184257000655634
0.02903089899882616
0.02805489800084615
0.028508392999356147
0.03074074600044696
0.02795246800087625
temps total pour 10 tâches de taille 1000 = 0.685513484002513

```

## Execution tache C++ (10 taches de taille 1000)
### configuration et  compilation

```bash
$ cmake -B build -S .
$ cmake --build build

```

### Execution

 Dans 4 terminaux tappez les commandes suivantes  :

1) premier terminal : lancer le serveur proxy :
```bash
   $ python proxy
   $ python manager.py
   $ python boss.py
   $ ./build/low_level
```
### Resultat :

```bash
Temps calcul  = 0.0288506
Temps calcul  = 0.0299842
Temps calcul  = 0.0287979
Temps calcul  = 0.0645198
Temps calcul  = 0.0292257
Temps calcul  = 0.0357392
Temps calcul  = 0.0289343
Temps calcul  = 0.0297993
Temps calcul  = 0.0288148
Temps calcul  = 0.0287492
temps total = 0.0287492

```


### Resultat en configuration release :
Pour accelere les calcul en C++ on peut passer le compilateur en mode release :
Dans un terminal tappez d'abord la commande

```bash
   cmake --build build --config Release
```

puis recompilez et executer

résulats :
```bash

Temps calcul  = 0.0292915
Temps calcul  = 0.0288215
Temps calcul  = 0.0289206
Temps calcul  = 0.0288103
Temps calcul  = 0.0313312
Temps calcul  = 0.049761
Temps calcul  = 0.0290078
Temps calcul  = 0.0299325
Temps calcul  = 0.0697193
Temps calcul  = 0.0286821
temps total = 0.0286821
```
On n'observe pas de différence significative avec ou sans le mode release pour le C++.
Cependant on observe que le C++ effectue la tache plus rapidement que le python


si vous avez cette erreur :
```bash
terminate called after throwing an instance of 'nlohmann::json_abi_v3_11_3::detail::type_error'
  what():  [json.exception.type_error.302] type must be number, but is null
```
relancez boss.py et low_level ( elle se produit de temps, je ne sais pas pourquoi)
