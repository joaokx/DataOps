import pandas as pd
from pymongo import MongoClient
from create_dataframes import carros_df, montadoras_df


client = MongoClient('localhost', 27017)
db = client['testdb']  


db['Carros'].insert_many(carros_df.to_dict('records'))
db['Montadoras'].insert_many(montadoras_df.to_dict('records'))



client.close()
