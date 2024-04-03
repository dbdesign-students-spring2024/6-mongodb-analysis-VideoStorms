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

# Select your database and collection
collection = connection[db_name][db_collection_name]

# the collection variable will be a reference to your collection
# Fetching the first 10 documents
docs = collection.find({}).limit(10)

# Iterating through the documents and printing them
for doc in docs:
    print(doc)

# Your MongoDB query
#query = {"$and": [{"beds": {"$gt": 2}}, {"neighborhood": "Your Neighborhood Here"}]}
#projection = {"_id": 0, "name": 1, "beds": 1, "review_scores_rating": 1, "price": 1}

# Execute the query and sort the results
#docs = collection.find(query, projection).sort("review_scores_rating", pymongo.DESCENDING)
