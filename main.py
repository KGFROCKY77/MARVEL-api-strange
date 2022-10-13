import requests
import pandas as pd 
import json 
import hashlib 
import time
import datetime
import string 
from asyncio.windows_events import NULL
from pandas import json_normalize
timestamp = datetime.datetime.now()
limit = 100
import argparse
parser = argparse.ArgumentParser(description="provide the private_key and public_key")
private_key = parser.add_argument('private_key',type=str,help='provide the private_key')
public_key = parser.add_argument('public_key',type=str,help='provide the public_key')

from activity2 import hash_params

url_1 = "http://gateway.marvel.com/v1/public/characters"

blank_list =[]
for i in string.ascii_uppercase:
    nameStartsWith = i 
    parameters = { "ts": timestamp, "apikey": public_key, "hash": hash_params(),
    "nameStartsWith": nameStartsWith, "limit": limit}
    response = requests.get(url_1,params=parameters)
    data_character = response.json()
    df_character= pd.json_normalize(data_character,record_path=['data','results'])
    blank_list.append(df_character)
df_required = pd.concat(blank_list)

df_new = df_required[['id','name','comics.available','stories.available','events.available']]
print(df_new)
# here we obtain dataframe containing 1398 rows and required columns(activity_2)


from activity3 import gen_dataframe
activity3_df = gen_dataframe(nameStartsWith='A',APIKEY = public_key, HASH = hash_params())

print (activity3_df)

# used the function gen_dataframe for completing activity_3(name of characters starting with A )
from activity4 import gen_filter
activity4_df = gen_filter(
    df_63= activity3_df,
    column_name = 'comics.available',
    filter = ['>',50]
)
print(activity4_df)
# used the function gen_filter to filter based on integer columns
