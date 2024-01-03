#setting up everything 
import requests as rq

cf_base_url = 'https://codeforces.com/api/'

def getUpcomingContestList() -> list:
    
    fres = []
    r = rq.get(cf_base_url + 'contest.list') # Warning. Big List
    for res in r.json()["result"]:
        if res["phase"] == "BEFORE":
            fres.append(res)

    return fres

# pretty print conetst list
def pp_contestlist(reslist):
    for i in reslist:
        print(i)

if __name__ == '__main__':
    pp_contestlist(getUpcomingContestList())