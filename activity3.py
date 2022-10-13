from asyncio.windows_events import NULL
import time
import datetime
import requests
import pandas as pd 
import json
from pandas import json_normalize
import hashlib


timestamp=datetime.datetime.now()
def gen_dataframe (nameStartsWith,APIKEY=NULL, HASH=NULL):
    if(APIKEY==NULL and HASH==NULL):
        raise Exception("NULL values not allowed")
    else:
        REQ_URL = "http://gateway.marvel.com/v1/public/characters"
       
        parameters = { "ts": timestamp, "apikey": APIKEY, "hash": HASH,
        "nameStartsWith": nameStartsWith}
        response = requests.get(REQ_URL,params=parameters)
        data_7 = response.json()
        df_7 = pd.json_normalize(data_7,record_path=['data','results'])
        df_new = df_7[['id','name','comics.available','stories.available','events.available']]
        return df_new



