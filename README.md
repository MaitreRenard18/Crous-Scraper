# Crous-Scraper

## Description
Crous scraper est un bot discord utilisant discord.py qui envoie un message en mp lorsqu'un logement du Crous se libère en utilisant les modules requests et BeautifulSoup.

# Installation
1. Clonez ce dépôt sur votre machine.
2. Installez les dépendances en exécutant : `pip install -r requirements.txt`.
3. Configurez les clés d'API Discord `main.py` en modifiant la variable `BOT_TOKEN`.

## Utilisation
Pour le faire marcher il suffit d'envoyer : `>start [URL de la recherche Crous]`

Par exemple `>start https://trouverunlogement.lescrous.fr/tools/31/search`  
Envera tout les logements du Crous disponible.  
Tandis que :  
`>start https://trouverunlogement.lescrous.fr/tools/31/search?bounds=1.8757578_47.9335389_1.9487114_47.8132802`  
Envera uniquement ceux d'Orléans.  

Pour arrêter la recherche il suffit d'envoyer : `>stop`  
