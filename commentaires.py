from constants import CHOIX_MENU,CHARACTERS, MONSTERS
from utils import user_choice
from variable import choice_menu, top_5_score, random_monster,hero_victim, wave_score, current_monster , hero_atk_damages
from db_init import collectionPlayers
import pymongo
import sys
import random


def main():
    print_options()
       
    
    
# afficher les options pour l'user
def print_options():
    # l'user choisi une option parmis les 3 (user_choice)
    choice_menu = user_choice(1, CHOIX_MENU)
    # si l'option est jouer
    if "Démarrer le jeu" in choice_menu :
        # lancer la sélection de personnage
        team_choice = user_choice(3, CHARACTERS)
        # lancer le jeu
        da_game(team_choice)
    # sinon si l'option est quitter
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
        current_monster = monster_generator()
        # lancer combat a mort
        death_battle(team_choice,current_monster)
        # score += wave_score
        score += wave_score
    # stocker le pseudo l'equipe et le score final dans la DB
    ...
    # lancer afficher les options pour l'user
    print_options()
    
# générer un monstre
def monster_generator():
    # indice du monstre = nb.random(0, len(collection)) ( il existe un fonction randmon choice)
    # random_monster_index = random.choice(list(MONSTERS.values()))
    # monstre généré = monstre.copy(indice du monstre)
    current_monster = random.choice(MONSTERS)
    # retourner le monstre généré
    return current_monster.copy()
    
# combat a mort
def death_battle(team,monster) :
    # tant que tout le monde de l'équipe n'est pas morte ou que le monstre n'est pas mort
    while not all(stats["DEAD"] for stats in team.values()) and not monster["DEAD"]:
        # lancer affichage des stats
        stats_in_fight(team, monster)
        # pour les personnages dans l'équipe qui ont DEAD = False
        for selected_hero, stats in team.items():
            if not stats["DEAD"] :    
                # lancer attaquer des heros
                heroes_attacking(stats, current_monster)
        # si le monstre n'est pas mort
        if monster["DEAD"] == False :
            # lancer attaque du monstre
            monster_attacking(hero_victim, current_monster)
        
# attaque des heros 
def heroes_attacking(hero, monster):
    # dgts =- (ATK hero - DEF monstre)
    heroes_atk_damages = max(0, hero["ATK"] - monster["DEF"])
    # PV =- heroes_atk_damdges
    monster["PV"] =- heroes_atk_damages
    # score = dégats au monstre
    wave_score =+ heroes_atk_damages
    # si les pv du monstre <= 0
    if monster["PV"] <= 0 :
        # on met les pv a 0
        monster["PV"] = 0
        # dead = True
        monster["DEAD"] = True
        
        
        
# attaque du monstre
def monster_attacking(hero, monster) :
    # choisir un indice aléatoire et le stocker
    hero_victim = random.choice(hero)
    # pv héro choisi = (ATK monstre - DEF héro choisi)
    hero_victim["PV"] = (monster["ATK"] - hero_victim["DEF"]) 
    # si les pv du hero choisi <= 0
    if hero_victim["PV"] <= 0 :
        # on met les pv a 0
        hero_victim["PV"] = 0 
        # dead = True
        hero_victim["DEAD"] = True
    
# affichage des stats
def stats_in_fight(hero_team, monstre) :
    print("--- ÉQUIPE ---")
    # pour les héros dans l'équipe
    for nom, stats in hero_team.items():
        # définir l'état du personage
        etat = " [ MORT]" if stats["DEAD"] else ""
        # afficher les stats et si il est mort
        print(f"{nom}{etat} - PV: {stats['PV']} | ATK: {stats['ATK']} | DEF: {stats['DEF']}")
    # affichage du monstre
    print("\n--- MONSTRE ---")
    # recuperer les stats du monstre
    monster_name = monstre.get("name", monstre.get("nom", "Monstre"))
    # afficher le nom et les pv du monstre
    print(f"{monster_name} - PV: {monstre['PV']} | ")
    
main()
# FAIRE SYSTEME SCORE