from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://nehakeswani:Tomandjerry@cluster0.mdmqekb.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


d = {
    "name" : "neha",
    "surname" : "keswani",
    "email" : "nkeswani14"
}
d = {
    "name" : "neha",
    "surname" : "keswani",
    "email" : "nkeswani14"
}
d = {
    "name" : "neha",
    "surname" : "keswani",
    "email" : "nkeswani14"
}
d = {
    "name" : "neha",
    "surname" : "keswani",
    "email" : "nkeswani14"
}


db = client['mongotest']
coll = db['test']
coll.insert_one(d)