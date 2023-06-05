from pymongo import MongoClient
import pymongo


MONGO_URI = 'mongodb://localhost/'


# Conexión a la base de datos
def dbConnection():
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['BienesyRaices']
    return db