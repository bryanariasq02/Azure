import getpass
import pymongo

DBAccountName = "prueba3bio"
DBAccountKey = getpass.getpass()

URI = "mongodb://" + DBAccountName + ":" + DBAccountKey + "@" + DBAccountName + ".mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@" + DBAccountKey + "@"
client  = pymongo.MongoClient(URI)

try:
    client.server_info() # validate connection string
except pymongo.errors.ServerSelectionTimeoutError:
    raise TimeoutError("error")
db_list = client.list_database_names()