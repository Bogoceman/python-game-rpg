from pymongo import MongoClient
from models import *
from variable import score, player_name

client = MongoClient("mongodb://localhost:27017/")
db = client["rpg_game"]
collectionMonsters = db["monsters"]
collectionCharacters = db["characters"]
collectionPlayers = db["players"]

if __name__ == "__main__":
    collectionCharacters.insert_many([{"name": name, **stats} for name, stats in characters.items()])
    collectionMonsters.insert_many([{"name": name, **stats} for name, stats in monsters.items()])