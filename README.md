# Crous-Scraper

## Description
Crous-Scraper est un bot Discord développé avec discord.py qui envoie un message privé lorsqu'un logement du Crous devient disponible. Il utilise les modules requests et BeautifulSoup pour effectuer le scrapping.

## Installation
1. Clonez ce dépôt sur votre machine.
2. Exécutez `run.bat` et saisissez vos clés d'API Discord pour démarrer le bot.

## Utilisation
Pour le faire marcher il suffit d'envoyer : `>start [URL de la recherche Crous]`

Par exemple `>start https://trouverunlogement.lescrous.fr/tools/31/search`.  
Enverra tous les logements du Crous disponibles.  
Si vous souhaitez limiter la recherche à une région spécifique, utilisez l'URL correspondante. Par exemple :  
`>start https://trouverunlogement.lescrous.fr/tools/31/search?bounds=1.8757578_47.9335389_1.9487114_47.8132802`.  
Enverra uniquement ceux d'Orléans. (Copiez simplement l'URL affichée lorsque vous effectuez votre recherche sur le site du Crous.)

Pour arrêter la recherche, envoyez : `>stop`.
