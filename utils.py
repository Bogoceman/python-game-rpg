from constants import INTRO_SCRIPT
from variable import score, player_name
from db_init import collectionPlayers, db, client

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
        
    # sélection les personnages a choisir 
        # demander a l'utilisateur quel personnage il veut choisir (3 personnages)
        # enregistrer la sélection des personnages dans la base de données du joueur

intro()