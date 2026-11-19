# afficher les options pour l'user
    # l'user choisi une option parmis les 3 (user_choice)
    # si l'option est jouer
        # lancer la sélection de personnage
        # lancer le jeu
    # sino si l'option est quitter 
        # lancer quitter le jeu
    # sinon si l'option est leaderboard
        # lancer afficher le leaderboard

#  afficher le leaderboard
    # on prend le top 5 de la DB
    # pour joueurs dans le top 5
        # afficher le nom, le score, les personnages de son équipe

# quitter le jeu
    # afficher un message triste
    # quitter le jeu
    
# le jeu
    # tant que l'equipe n'est pas morte (peut être le remplacer par un while True ?)
        # lancer générer un monstre 
        # lancer combat a mort
        # score += wave_score
    # stocker le pseudo l'equipe et le score final dans la DB
    # lancer afficher les options pour l'user
    
# générer un monstre
    # indice du monstre = nb.random(0, len(collection)) ( il existe un fonction randmon choice)
    # monstre généré = monstre.copy(indice du monstre)
    # retourner le monstre généré
    
# combat a mort
    # tant que tout le monde de l'équipe n'est pas morte ou que le monstre n'est pas mort
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
    # afficher tout les héros avec leurs stats et si ils sont encore en vie
    # afficher le nom et les pv du monstre