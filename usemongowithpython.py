import pymongo

# Setting up the connection
connection = pymongo.MongoClient("localhost", 27017,
                                 username="rg4071",
                                 password="_6aEZyyzQ3",
                                 authSource="rg4071")
collection = connection["rg4071"]["listings"]

# Fetching the first 10 documents
docs = collection.find({}).limit(10)

# Iterating through the documents and printing them
for doc in docs:
    print(doc)
