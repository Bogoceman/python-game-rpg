import pymongo
import sys
from constants import INTRO_SCRIPT, GAME_CHOICE
from variable import score, player_name, choice_user, top_5_score, choice_team
from db_init import collectionPlayers, collectionCharacters


# selection de si on veut jouer, voir les scores, ou quitter le jeu
def choice() :
    # tant que infini
    while True :
        # affichage des options 
        print(f"{GAME_CHOICE}")
        # demander a l'utilisateur quel option il veut
        choice_user = (input("Que choisissez vous ? "))
        # faire un test du choix du l'utilisateur
        if choice_user.isdigit():
            choice_user = int(choice_user)
            if 1 <= choice_user <= 3 :
                return choice_user
            else :
                print("Rentrez 1, 2 ou 3 pour continuer")
        # si test pas bon ça recommence
        else :
            print("Rentrez 1, 2 ou 3 pour continuer")
    

# introduction du jeu 
def intro():
    # texte d'introduction
    print(f"{INTRO_SCRIPT}")
    # demander au joueur quel est son pseudo 
    player_name = input("Quel est votre nom ?")
    # boucle tant que le pseudo n'est pas valide (entre 3 et 15 caractères STR)
    while len(player_name) < 3 or len(player_name) > 15 :
        player_name = input("Veuillez renseigner un pseudo entre 3 et 15 caractères :")
    # stocker le pseudo et le score du joueur dans la BDD
    collectionPlayers.insert_one({"name": player_name, "score": [score],"characters": []})
    # retourner le pseudo 
    return player_name


# option pour afficher le leaderboard
def leaderboard() :
    top_5_score = collectionPlayers.find().sort("score", pymongo.DESCENDING).limit(5)
    for players in top_5_score :
        print(f"{players['name']} : {players['scores']} : {players['personnages']}") # dans la db la team s'appelle "personnages" a corriger 

# option pour quitter le jeu
def quit_game() :
    print(":'(")
    sys.exit()

# sélection les personnages a choisir 
def team_selection() :
    # création du dictionnaire de la team
    team = {}
    # demander a l'utilisateur quel personnage il veut choisir (3 personnages)
    print("Choisissez vos compagnons")
    for index, ally in enumerate(collectionCharacters.find(), start=1) :
        print(f"{index} - {ally['name']} : Attaque {ally['ATK']} | Défense {ally['DEF']} | Point de Vie {ally['PV']}")
    # tant que l'equipe n'a pas 3 joueurs
    while team < 3 :
        # ajouter le personnage a la team et incrémenter de 1 a chaques boucles
        choice_team = int(input(f"Entrez le numéro du personnage ({len(team) + 1}/3) : "))
        # ajouter le personnage a la team et le retirer du dictionnaire
        team
    # enregistrer la sélection des personnages dans la base de données du joueur
    # enregistrer la team dans la bdd
    
team_selection()