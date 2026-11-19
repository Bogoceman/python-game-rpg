from constants import CHARACTERS
import copy

# clone d'un dictionnaire
def cloning(original_dict):
    # créer le clone avec .deepcopy
    clone = copy.deepcopy(original_dict)
    return clone

# l'utilisateur rentre son choix et le bon (test)
def check_user_choice(choosen_list):
    while True:
        user_input_choice = input("Sélectionnez votre choix : ")
        if user_input_choice.isdigit():
            index = int(user_input_choice) - 1
            if 0 <= index < len(choosen_list):
                return choosen_list.pop(index)
        print("Choix invalide, entrez un numéro de la liste.")

# l'utilisateur doit choisir
def user_choice(number_choice, characters_dict):
    # Dictionnaire des personnages choisis (avec leurs stats clonées)
    available_names = list(characters_dict.keys())
    selected_choices = {}

    while len(selected_choices) < number_choice:
        for number, name in enumerate(available_names, start=1):
            print(f"{number} - {name}")

        selected = check_user_choice(available_names)

        # Connexion avec cloning() : on clone les stats du personnage choisi
        selected_choices[selected] = cloning(characters_dict[selected])

    return selected_choices

# --- Utilisation ---
#mon_equipe = user_choice(3, CHARACTERS)
#print("Votre équipe :", mon_equipe)