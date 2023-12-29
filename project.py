#setting up everything 
from dotenv import load_dotenv
import os
import requests
import hashlib
import random
from datetime import datetime

#generating unix time stamp 
current_time = datetime.now()
unix_timestamp=int(current_time.timestamp())

#print("Current System Time:", unix_timestamp)

#loading Env's
load_dotenv()

api_key = os.getenv("API_KEY")
api_secret = os.getenv("secret")

#print(f"API Key: {api_key}")
#print(f"API Secret: {debug_mode}")

method_name="contest.list"
rand = str(random.randint(100000, 999999))

#constructing the string to be hashed 
hash1=f"{rand}/{method_name}?apiKey={api_key}&time={unix_timestamp}#{api_secret}"

# SHA-512 hash
hash_code=hashlib.sha512(hash1.encode()).hexdigest()



#constructing the url
api_url = f"https://codeforces.com/api/{method_name}?apiKey={api_key}&time={unix_timestamp}&apiSig={rand}{hash_code}"



#Make the Api request 

response=requests.get(api_url)
print(response.json())

