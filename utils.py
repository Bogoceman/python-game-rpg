import sys
from constants import INTRO_SCRIPT, GAME_CHOICE
from variable import score, player_name, choice_user
from db_init import collectionPlayers


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
    

# option pour quitter le jeu
def quit_game() :
    print(":'(")
    sys.exit()
    

choice()            

# sélection les personnages a choisir 
    # demander a l'utilisateur quel personnage il veut choisir (3 personnages)
    # enregistrer la sélection des personnages dans la base de données du joueur