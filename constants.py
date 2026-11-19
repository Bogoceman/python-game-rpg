INTRO_SCRIPT = "Bienvenue dans Le Donjon Infernal. \nVous allez devoir vaincre des hordes d'ennemies à travers ce Donjon infinie"
GAME_CHOICE = "Que voulez vous faire ? \n1.Jouer \n2.Voir les scores \n3.quitter le jeu"

CHARACTERS = {
	"Guerrier": {"ATK": 15, "DEF": 10, "PV": 100, "DEAD": False},
	"Mage": {"ATK": 20, "DEF": 5, "PV": 80, "DEAD": False},
	"Archer": {"ATK": 18, "DEF": 7, "PV": 90, "DEAD": False},
	"Voleur": {"ATK": 22, "DEF": 8, "PV": 85, "DEAD": False},
	"Paladin": {"ATK": 14, "DEF": 12, "PV": 110, "DEAD": False},
	"Sorcier": {"ATK": 25, "DEF": 3, "PV": 70, "DEAD": False},
	"Chevalier": {"ATK": 17, "DEF": 15, "PV": 120, "DEAD": False},
	"Moine": {"ATK": 19, "DEF": 9, "PV": 95, "DEAD": False},
	"Berserker": {"ATK": 23, "DEF": 6, "PV": 105, "DEAD": False},
	"Chasseur": {"ATK": 16, "DEF": 11, "PV": 100, "DEAD": False},
}

MONSTERS = [
	{"NOM":"Gobelin" ,"ATK": 10, "DEF": 5, "PV": 50, "DEAD": False},
	{"NOM":"Orc" ,"ATK": 20, "DEF": 8, "PV": 120, "DEAD": False},
	{"NOM":"Dragon" ,"ATK": 35, "DEF": 20, "PV": 300, "DEAD": False},
	{"NOM":"Zombie" ,"ATK": 12, "DEF": 6, "PV": 70, "DEAD": False},
	{"NOM":"Troll" ,"ATK": 25, "DEF": 15, "PV": 200, "DEAD": False},
	{"NOM":"Spectre" ,"ATK": 18, "DEF": 10, "PV": 100, "DEAD": False},
	{"NOM":"Golem" ,"ATK": 30, "DEF": 25, "PV": 250, "DEAD": False},
	{"NOM":"Vampire" ,"ATK": 22, "DEF": 12, "PV": 150, "DEAD": False},
	{"NOM":"Loup-garou", "ATK": 28, "DEF": 18, "PV": 180, "DEAD": False},
	{"NOM":"Squelette" ,"ATK": 15, "DEF": 7, "PV": 90, "DEAD": False},
]

CHOIX_MENU = {
    "Démarrer le jeu" : {"text" : "Démarrer le jeu"},
    "Leaderboard" : {"text" : "Leaderboard"},
    "Quiter le jeu" : {"text" : "Quiter le jeu"}
}