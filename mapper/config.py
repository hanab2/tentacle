import pymongo

# --------------------------->config<-------------------------#
host = 'localhost'
port = 27017

###############################################################
client = pymongo.MongoClient(host=host, port=port)
