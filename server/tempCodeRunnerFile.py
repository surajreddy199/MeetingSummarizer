mongoURI = f"mongodb+srv://shivam:Avengers123@mycluster.eafse.mongodb.net/TLDWrite?retryWrites=true&w=majority"
client = MongoClient(mongoURI)
fs = gridfs.GridFS(client['TLDWrite'], "uploads")