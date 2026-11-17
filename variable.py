import pymongo
from db_init import collectionPlayers

score = 0
player_name = ""
choice_user = 0
top_5_score = collectionPlayers.find().sort("score", pymongo.DESCENDING).limit(5)

print(f"{top_5_score}")