from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = ("mongodb+srv://longdvgcs220434:daovinhlong@web2cluster.6tftv.mongodb.net/?retryWrites=true&w=majority&appName"
       "=Web2Cluster")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection

db = client.bookCRUD_db
collection = db["bookCRUD_data"]

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
