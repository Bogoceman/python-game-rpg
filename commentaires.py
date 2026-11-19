from constants import CHOIX_MENU,CHARACTERS, MONSTERS
from utils import user_choice
from variable import choice_menu, top_5_score, random_monster, wave_score,
from db_init import collectionPlayers
import pymongo
import sys
import random

# afficher les options pour l'user
def print_options():
    # l'user choisi une option parmis les 3 (user_choice)
    choice_menu = user_choice(1, CHOIX_MENU)
    # si l'option est jouer
    if "Démarrer le jeu" in choice_menu :
        # lancer la sélection de personnage
        team_choice = user_choice(3, CHARACTERS)
        # lancer le jeu
    # sino si l'option est quitter
    elif "Leaderboard" in choice_menu : 
        # lancer afficher le leaderboard
        leaderboard()
    # sinon si l'option est leaderboard
    elif "Quitter" in choice_menu:
        # lancer quitter le jeu
        left_da_game()
        
#  afficher le leaderboard
def leaderboard() :
    # on prend le top 5 de la DB
    top_5_score = collectionPlayers.find().sort("score", pymongo.DESCENDING).limit(5)
    # pour joueurs dans le top 5
    for players in top_5_score :
        # afficher le nom, le score, les personnages de son équipe
        print(f"{players['name']} : {players['scores']} : {players['personnages']}")
        
# quitter le jeu
def left_da_game():
    # afficher un message triste
    print(":'(")
    # quitter le jeu
    sys.exit()

# le jeu
def da_game(team_choice) :
    # tant que l'equipe n'est pas morte
    while not all(stats["DEAD"] for stats in team_choice.values()):
        # lancer générer un monstre 
        monster_generator()
        # lancer combat a mort
        # score += wave_score
        score += wave_score
    # stocker le pseudo l'equipe et le score final dans la DB
    # lancer afficher les options pour l'user
    
# générer un monstre
def monster_generator():
    # indice du monstre = nb.random(0, len(collection)) ( il existe un fonction randmon choice)
    random_monster_index = random.choice(MONSTERS)
    # monstre généré = monstre.copy(indice du monstre)
    current_monster = MONSTERS.copy(random_monster_index)
    # retourner le monstre généré
    return current_monster
    
# combat a mort
def death_battle(team,monster) :
    # tant que tout le monde de l'équipe n'est pas morte ou que le monstre n'est pas mort
    while not all(stats["DEAD"] for stats in team.values()) and not monster["DEAD"]:
        # lancer affichage des stats
        
        # pour les personnages dans l'équipe qui ont DEAD = False
            # lancer attaquer des heros
        # si le monstre n'est pas mort
            # lancer attaque du monstre
        
# attaque des heros 
    # pv monstre = (ATK hero - DEF monstre)
    
# attaque du monstre 
    # choisir un indice aléatoire et le stocker
    # pv héro choisi = (ATK monstre - DEF héro choisi)
    
# affichage des stats
def stats_in_fight(hero_team, monstre) :
    print("--- ÉQUIPE ---")
    # pour les héros dans l'équipe
    for heros in hero_team :
        # définir l'état du personage
        etat = " [ MORT]" if stats["DEAD"] else ""
        # afficher les stats et si il est mort
        print(f"{nom}{etat} - PV: {stats['PV']} | ATK: {stats['ATK']} | DEF: {stats['DEF']}")
    # affichage du monstre
    print("\n--- MONSTRE ---")
    # afficher tout les héros avec leurs stats, si ils sont morts
    print(f"{monstre['nom']} - PV: {monstre['PV']}")
    
    # afficher le nom et les pv du monstre
    
    
# FAIRE SYSTEME SCORE