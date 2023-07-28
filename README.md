# Crous-Scraper

## Description
Crous-Scraper est un bot Discord utilisant discord.py qui envoie un message en MP lorsqu'un logement du Crous se libère en utilisant les modules requests et BeautifulSoup.

## Installation
1. Clonez ce dépôt sur votre machine.
2. Configurez les clés d'API Discord `main.py` en modifiant la variable `BOT_TOKEN`.
3. Exécutez `run.bat` pour démarrer le bot.

## Utilisation
Pour le faire marcher il suffit d'envoyer : `>start [URL de la recherche Crous]`

Par exemple `>start https://trouverunlogement.lescrous.fr/tools/31/search`.  
Enverra tous les logements du Crous disponibles.  
Tandis que :  
`>start https://trouverunlogement.lescrous.fr/tools/31/search?bounds=1.8757578_47.9335389_1.9487114_47.8132802`.  
Enverra uniquement ceux d'Orléans. (Vous avez juste à copier-coller l'URL qui s'affiche lorsque vous effectuez votre recherche sur le site du Crous.)

Pour arrêter la recherche, envoyez : `>stop`.
