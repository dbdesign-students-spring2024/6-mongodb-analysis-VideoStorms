import pymongo

# Replace these variables with your actual database information
db_host = "class-mongodb.cims.nyu.edu"
db_port = 27017
db_username = "rg4071"  # Your NYU ID or username for MongoDB
db_password = "P5rZ6aci"  # Your MongoDB password
db_name = "rg4071"  # Your database name, probably your NYU ID
db_collection_name = "listings"

# Connect to MongoDB
connection = pymongo.MongoClient(db_host, db_port,
                                 username=db_username,
                                 password=db_password,
                                 authSource=db_name)

# Select your database and collection
collection = connection[db_name][db_collection_name]

# Your MongoDB query
query = {"$and": [{"beds": {"$gt": 2}}, {"neighborhood": "Your Neighborhood Here"}]}
projection = {"_id": 0, "name": 1, "beds": 1, "review_scores_rating": 1, "price": 1}

# Execute the query and sort the results
docs = collection.find(query, projection).sort("review_scores_rating", pymongo.DESCENDING)

# Print the results
for doc in docs:
    print(doc)
