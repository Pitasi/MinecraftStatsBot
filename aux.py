#!/usr/bin/python3

import json
from config import *

users = {}






with open(usercache_file) as f:
    usercache = json.load(f)

for i in usercache:
    with open(json_path % i['uuid']) as f:
        users[i['name']] = json.load(f)





def users_number():
    return len(users)


def jumps(user):
    try:
        return user["stat.jump"]
    except KeyError:
        return 0

def deaths(user):
    try:
        return user["stat.deaths"]
    except KeyError:
        return 0
        

def killed_by(user, entity):
    if entity == "skeleton":
        try:
            return user["stat.entityKilledBy.Skeleton"]
        except KeyError:
            return 0
    elif entity == "zombie":
        try:
            return user["stat.entityKilledBy.Zombie"]
        except KeyError:
            return 0
    elif entity =="enderman":
        try:
            return user["stat.entityKilledBy.Enderman"]  
        except KeyError:
            return 0
    else:
        raise KeyError("Entity not valid. Please use 'skeleton', 'zombie', or 'enderman'.")




#
# Printers
#

def print_jumps():
    res = []
    for u in users:
        res.append((u, jumps(users[u])))
    res.sort(key=lambda tup: tup[1], reverse=True)
    testo = ""
    for i in range(0, len(res)):
        testo += "%s) *%s* ha effettuato *%s* salti.\n" % (i+1, res[i][0], res[i][1])
    return testo


def print_deaths():
    res = []
    for u in users:
        res.append((u, deaths(users[u])))
    res.sort(key=lambda tup: tup[1], reverse=True)
    testo = ""
    for i in range(0, len(res)):
        testo += "%s) *%s* è morto *%s* volte.\n" % (i+1, res[i][0], res[i][1])
    return testo


def print_killed_by(entity):
    res = []
    for u in users:
        res.append((u, killed_by(users[u], entity)))
    res.sort(key=lambda tup: tup[1], reverse=True)
    testo = ""
    for i in range(0, len(res)):
        testo += "%s) *%s* è morto *%s* volte.\n" % (i+1, res[i][0], res[i][1])
    return testo


