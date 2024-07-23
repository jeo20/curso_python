from pymongo import MongoClient

#Base de datos local
#db_client = MongoClient().local # si no le paso parametro se conecta a localhost

#Base de datos remota
db_client = MongoClient('mongodb+srv://jeo2k1:Python2024@cluster0.euzcrke.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0').test
