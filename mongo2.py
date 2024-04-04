import pymongo

db_host = "class-mongodb.cims.nyu.edu"
db_port = 27017
db_username = "rg4071"  
db_password = "P5rZ6aci"  
db_name = "rg4071"  
db_collection_name = "listings"

connection = pymongo.MongoClient(db_host, db_port,
                                 username=db_username,
                                 password=db_password,
                                 authSource=db_name)

collection = connection[db_name][db_collection_name]


result = collection.find(
    {'neighbourhood_cleansed': 'Leopoldstadt', 'beds': {'$gt': 2}},
    {'name': 1, 'beds': 1, 'review_scores_rating': 1, 'price': 1}
).sort('review_scores_rating', -1)

# Iterate over and print each document in the result
for doc in result:
    print(doc)