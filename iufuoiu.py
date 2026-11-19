import pymongo
import sys
from constants import INTRO_SCRIPT, GAME_CHOICE, CHARACTERS
from variable import score, player_name, choice_user, top_5_score, choice_team, add_team, usefull_data
from db_init import collectionPlayers, collectionCharacters, client
# initialisation de la liste team
team = []


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
def team_selection():
    # Récupérer les personnages depuis la base de données dans une liste
    allies = list(collectionCharacters.find())
    print("Choisissez vos compagnons")
    for index, ally in enumerate(allies, start=1):
        print(f"{index} - {ally['name']} : Attaque {ally['ATK']} | Défense {ally['DEF']} | Point de Vie {ally['PV']}")
    # Tant que l'équipe n'a pas 3 joueurs
    while len(team) < 3:
        usefull_data = input(f"Entrez le numéro du personnage ({len(team) + 1}/3) : ")
        # Vérifier que la saisie est bien un chiffre entre 1 et le nombre de personnages
        if not (usefull_data.isdigit() and 1 <= int(usefull_data) <= len(allies)):
            print(f"Erreur : veuillez entrer un chiffre entre 1 et {len(allies)}.")
            continue  # Recommence la boucle
        choice_team = int(usefull_data)
        choosen_champ = allies[choice_team - 1]
        # Vérifier que le personnage n'est pas déjà dans l'équipe
        if choosen_champ in team:
            print("Vous avez déjà sélectionné ce personnage, choisissez-en un autre.")
            continue
        # Ajouter le personnage à la team
        team.append(choosen_champ)
        print(f"Vous avez sélectionné : {choosen_champ['name']}")

    return team

    
team_selection()
print(team)


