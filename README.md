# TP multithreading
## Arnaud grondin

Le but du tp

### execution tache C++
### ouvrez 4 terminaux


1) premier terminal : lancer le serveur proxy :
```bash
   $ python proxy
```
2) second terminal lancer le manager qui va gerer les requetes :
```bash
    $ python manager.py
```
3) troisième terminal : lancer le processus qui va donner une tache
```bash
    $ python boss.py
```
4) Quatrième terminal :  lancer le programme c++ qui va recevoir la tache et l'effectuer :
```bash
    ./build/low_level
```
si vous avez cette erreur :
```bash
terminate called after throwing an instance of 'nlohmann::json_abi_v3_11_3::detail::type_error'
  what():  [json.exception.type_error.302] type must be number, but is null
```
relancez boss.py et low_level ( elle se produit de temps, je ne sais pas pourquoi)


résultat sur 10 éxécution en compilation standard:
Temps calcul  = 1.7886e-05
Temps calcul  = 8.4299e-05
Temps calcul  = 8.286e-05
Temps calcul  = 8.5436e-05
Temps calcul  = 0.000150105
Temps calcul  = 8.6123e-05
Temps calcul  = 8.2097e-05
Temps calcul  = 8.2741e-05
Temps calcul  = 6.2021e-05
Temps calcul  = 8.3591e-05


résultats après avoir mis le build type en mode release :
```bash
cmake --build build --config Release
```
Temps calcul  = 8.3318e-05
Temps calcul  = 8.1209e-05
Temps calcul  = 8.5833e-05
Temps calcul  = 8.3762e-05
Temps calcul  = 8.4917e-05
Temps calcul  = 8.3076e-05
Temps calcul  = 8.7068e-05
Temps calcul  = 8.252e-05
Temps calcul  = 8.2937e-05
Temps calcul  = 1.7283e-05
