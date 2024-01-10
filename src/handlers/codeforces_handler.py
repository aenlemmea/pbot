# setting up everything

import json
import pprint
import requests as rq

from model.contest import Contest

cf_base_url = "https://codeforces.com/api/"


async def getUpcomingContestList():
    fres = []
    r = rq.get(cf_base_url + "contest.list")  # Warning. Big List
    for res in r.json()["result"]:
        if res["phase"] == "BEFORE":
            deserialized_contest = Contest(
                res["id"],
                res["name"],
                res["type"],
                res["phase"],
                res["frozen"],
                res["durationSeconds"],
                res["startTimeSeconds"],
                res["relativeTimeSeconds"],
            )
            fres.append(deserialized_contest)

    return fres


# TODO: pretty print conetst list
def pp_contestlist(reslist):
    for i in reslist:
        pprint(i)
