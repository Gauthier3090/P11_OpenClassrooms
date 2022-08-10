# Améliorez une application Web Python par des tests et du débogage

![](https://camo.githubusercontent.com/7c691d06ed3e830244e052e43bb63780a25f0be9c7446cd4bea9f638dae92c99/68747470733a2f2f6f6e617465737465706f7572746f692e636f6d2f77702d636f6e74656e742f75706c6f6164732f323032302f30322f4c6f676f5f6f70656e636c617373726f6f6d735f6f6e617465737465706f7572746f692e6a7067)

# Résumé du projet

Plateforme de réservation de places à des compétitions de force pour l'entreprise Güdlft.
L'objectif du projet est de corriger les erreurs et bugs présents dans le projet ainsi
que d'implémenter de nouvelles fonctionnalités.

# Démarrer le projet

````Bash
git clone https://github.com/Gauthier3090/P9_OpenClassrooms.git p11_gauthier
cd p11_gauthier
````
## Windows

La création d'environnements virtuels est faite en exécutant la commande venv :

````Bash
python -m venv \path\to\new\virtual\venv
````

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

````Bash
.\venv\Scripts\activate.bat
pip install -r requirements.txt
````

Pour lancer le serveur Flask:

````Bash
$env:FLASK_APP = "server.py"
flask run
````

Dans le navigateur de votre choix, se rendre à l'adresse http://127.0.0.1:5000/

## Unix

La création d'environnements virtuels est faite en exécutant la commande venv :

````Bash
python3 -m venv \path\to\new\virtual\venv
````

Pour commencer à utiliser l’environnement virtuel, il doit être activé :

````Bash
source venv/bin/activate
pip install -r requirements.txt
````

Pour lancer le serveur Flask:

````Bash
$env:FLASK_APP = "server.py"
flask run
````

Dans le navigateur de votre choix, se rendre à l'adresse http://127.0.0.1:5000/

## Tests

Les tests unitaires et d'intégration sont exécutés grâce à Pytest
Pour effectuer l'ensemble des tests unitaires, entrer la commande :

````Bash
pytest tests
````

## Test de performances
Il est possible d'effectuer un test de performance grâce au module Locust. 
Pour lancer le serveur de test, entrer la commande :

````Bash
locust -f .\tests\performance_testing\locustfile.py --web-host=localhost
````
