#setting up everything 
from dotenv import load_dotenv
import os
import requests as rq
import hashlib
import random
from datetime import datetime


#loading Env's
load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("secret")
cf_base_url = 'https://codeforces.com/api/'

def getContestList():
    
    r = rq.get(cf_base_url + 'contest.list') # Warning. Big List
    for res in r.json()["result"]:
        if res["phase"] == "BEFORE":
            print(res)

# pretty print conetst list
def pp_contestlist():
    pass

if __name__ == '__main__':
    getContestList()