from constants import CHARACTERS
import copy

choice = {}
# clone d'un dictionnaire
def cloning(original_name):
    #créer le clone avec .deepcopy
    clone = copy.deepcopy(original_name)
    # return clone
    return clone
   
# l'utilisateur rentre son choix et le bon (test)
def check_user_choice(choosen_list):
    while True:
        # l'utilisateur rentre son choix
        user_input_choice = input("Sélectionnez votre choix : ")
        # si son choix est un nombre valide dans la liste
        if user_input_choice.isdigit():
            # on enlève 1 car la liste commence à partir de 0
            index = int(user_input_choice) - 1
            if 0 <= index < len(choosen_list):
                # retirer le choix de la liste et le retourner
                return choosen_list.pop(index)
        # sinon, afficher message d'erreur et recommencer
        print("Choix invalide, entrez un numéro de la liste.")


# l'utilisateur doit choisir
def user_choice(number_choice, characters_dict):
    # Liste des personnages choisis
    choice = []
      # Liste des noms disponibles
    available_names = list(characters_dict.keys())
    # tant que les choix ne sont pas complets
    while len(choice) < number_choice:
        # afficher les choix à l'utilisateur
        for number, name in enumerate(available_names, start=1):
            print(f"{number} - {name}")
        # l'utilisateur rentre son choix et le bon (test)
        selected = check_user_choice(available_names)
        # ajouter le choix à la liste des choix
        choice.append(selected)
    # retourner la liste des choix
    return choice


mon_equipe = user_choice(3, CHARACTERS)
print("Votre équipe :", mon_equipe)