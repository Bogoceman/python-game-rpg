import pymongo
import sys
from constants import INTRO_SCRIPT, GAME_CHOICE, CHARACTERS
from variable import score, player_name, choice_user, top_5_score, choice_team, add_team, usefull_data
from db_init import collectionPlayers, collectionCharacters, client
# initialisation de la liste team


# selection de si on veut jouer, voir les scores, ou quitter le jeu
    # tant que infini
        # affichage des options 
        # demander a l'utilisateur quel option il veut
        # faire un test du choix du l'utilisateur
        # si test pas bon ça recommence
    

# sélection d'une option parmi des chiffres

# introduction du jeu 
    # texte d'introduction
    # demander au joueur quel est son pseudo 
    # boucle tant que le pseudo n'est pas valide (entre 3 et 15 caractères STR)
    # stocker le pseudo et le score du joueur dans la BDD
    # retourner le pseudo 


# option pour afficher le leaderboard
    # prendre le top 5 des joueurs de la base de donnée
    #  pour chaques joueurs dans le top 5
        # afficher le pseudo du joueur avec son équipe et son score

# option pour quitter le jeu
    # afficher message triste
    
# sélection les personnages a choisir 
    # Récupérer les personnages depuis la base de données dans une liste
    # Tant que l'équipe n'a pas 3 joueurs
        # afficher les personnages que l'on peut jouer
        # Vérifier que la saisie est bien un chiffre entre 1 et le nombre de personnages
            # si bon
                # Vérifier que le personnage n'est pas déjà dans l'équipe
                    #si bon
                        # Ajouter le personnage à la team
            # sinon message d'erreur
    # retourner l'équipe 
    # enregistrer les personnages de l'équipe dans la base de donnée
    # afficher l'équipe du joueur
    
    