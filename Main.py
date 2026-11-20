from constants import CHOIX_MENU,CHARACTERS, MONSTERS
from utils import user_choice
from db_init import collectionPlayers
import variable
import pymongo
import sys
import random


def main():
    try:
        print_options()
    except (KeyboardInterrupt, EOFError):
        print("\nInterruption détectée.")
        left_da_game()
       
# demander au joueur son pseudo
def asking_username():
    while True:
        try:
            # on demande au joueur de rentrer un pseudo valide
            player_name = input("Veuillez renseigner un pseudo entre 3 et 15 caractères :")
        except (KeyboardInterrupt, EOFError):
            raise
        # on vérifie si le pseudo est bon
        if 3 <= len(player_name) <= 15:
            variable.player_name = player_name
            # on retourne le pseudo
            return player_name
        print("Le pseudo doit contenir entre 3 et 15 caractères.")
            
# afficher les options pour l'user
def print_options():
    # l'user choisi une option parmis les 3 (user_choice)
    choice_menu = user_choice(1, CHOIX_MENU)
    # si l'option est jouer
    if "Démarrer le jeu" in choice_menu :
        # l'user rentre son pseudo
        asking_username()
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
    # lancer affiche les 5 meilleurs joueurs
    get_leaderboard(top_5_score)

# affiche les 5 meilleurs joueurs    
def get_leaderboard(top_5_score) :    
    # pour joueurs dans le top 5
    for players in top_5_score :
        # afficher le nom, le score, les personnages de son équipe
        score = players.get("score", 0)
        if isinstance(score, list):
            score = score[0] if score else 0
        # on récupère l'équipe des meilleurs jouers 
        team = players.get("team", players.get("personnages", []))
        # récupère des stats des joueurs et on les mets dans une liste selon les conditions 
        team_names = [character.get("name", str(character))
            if isinstance(character, dict)
            else str(character)
            for character in team]
        # on affiche les stats des joueurs du top 5
        print(f"{players.get('name', 'Inconnu')} : {score} : {', '.join(team_names)}")
    print_options()
        
# quitter le jeu
def left_da_game():
    # afficher un message triste
    print(":'(")
    # quitter le jeu
    sys.exit()

# le jeu
def da_game(team_choice) :
    score = 0

    # tant que l'equipe n'est pas morte
    while not all(stats["DEAD"] for stats in team_choice.values()):
        # lancer générer un monstre 
        current_monster = monster_generator()
        # lancer combat a mort
        score += death_battle(team_choice, current_monster)
    # afficher le score final
    print(f"{score}")        
    # stocker le pseudo l'equipe et le score final dans la DB
    collectionPlayers.insert_one({
        "name": variable.player_name,
        "score": score,
        "team": list(team_choice.keys())
    })
    # lancer afficher les options pour l'user
    print_options()
    
# générer un monstre
def monster_generator():
    # monstre généré = monstre.copy(indice du monstre)
    current_monster = random.choice(MONSTERS)
    # retourner le monstre généré
    return current_monster.copy()
    
# combat a mort
def death_battle(team,monster) :
    wave_score = 0

    # tant que tout le monde de l'équipe n'est pas morte ou que le monstre n'est pas mort
    while not all(stats["DEAD"] for stats in team.values()) and not monster["DEAD"]:
        # lancer affichage des stats
        stats_in_fight(team, monster)
        # pour les personnages dans l'équipe qui ont DEAD = False
        for _, stats in team.items():
            if not stats["DEAD"] :    
                # lancer attaquer des heros
                wave_score += heroes_attacking(stats, monster)
        # si le monstre n'est pas mort
        if not monster["DEAD"]:
            # lancer attaque du monstre
            monster_attacking(team, monster)
    # on retourne la valeur
    return wave_score
        
# attaque des heros 
def heroes_attacking(hero, monster):
    # dgts =- (ATK hero - DEF monstre)
    heroes_atk_damages = max(0, hero["ATK"] - monster.get("DEF", 0))
    # PV =- heroes_atk_damdges
    monster["PV"] = max(0, monster["PV"] - heroes_atk_damages)
    # si les pv du monstre <= 0
    if monster["PV"] <= 0 :
        # on met les pv a 0
        monster["PV"] = 0
        # dead = True
        monster["DEAD"] = True
    # on retourne la valeur
    return heroes_atk_damages
        
        
        
# attaque du monstre
def monster_attacking(hero, monster) :
    # choisir parmi les héros encore vivants
    alive_heroes = [stats for stats in hero.values() if not stats["DEAD"]]
    if not alive_heroes:
        return

    hero_victim = random.choice(alive_heroes)
    # pv héro choisi = (ATK monstre - DEF héro choisi)
    damages = max(0, monster["ATK"] - hero_victim["DEF"])
    hero_victim["PV"] = max(0, hero_victim["PV"] - damages)
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
        etat = " [MORT]" if stats["DEAD"] else ""
        # afficher les stats et si il est mort
        print(f"{nom}{etat} - PV: {stats['PV']} | ATK: {stats['ATK']} | DEF: {stats['DEF']}")
    # affichage du monstre
    print("\n--- MONSTRE ---")
    # recuperer les stats du monstre
    monster_name = monstre.get("name", monstre.get("NOM", monstre.get("nom", "Monstre")))
    # afficher le nom et les pv du monstre
    print(f"{monster_name} - PV: {monstre['PV']} | ")
    
if __name__ == "__main__":
    main()