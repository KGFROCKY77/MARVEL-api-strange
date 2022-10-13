import requests
import pandas as pd 
import json 
import hashlib 
import time
import datetime
import string 
from pandas import json_normalize
timestamp = datetime.datetime.now()
limit = 100
import argparse
parser = argparse.ArgumentParser(description="provide the private_key and public_key")
private_key = parser.add_argument('private_key',type=str,help='provide the private_key')
public_key = parser.add_argument('public_key',type=str,help='provide the public_key')


def hash_params():
    hash_md5 = hashlib.md5()
    hash_md5.update(f'{timestamp}{private_key}{public_key}'.encode('utf-8'))
    hashe_params = hash_md5.hexdigest()
    return hashe_params



