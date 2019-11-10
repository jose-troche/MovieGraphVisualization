#!/usr/local/bin/python3

import csv, json, re

itemRegex = re.compile(r'\{(.*?)\}')

def parseNumber(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

def parseJsonStr(jsonStr):
    array = []

    for item in itemRegex.findall(jsonStr):
        print('===')
        print(item)
        itemHash = {}
        for pair in item.split(", '"):
            #print('+++')
            #print(pair)
            parts = pair.split("': ")

            if (len(parts) < 2):
                itemHash[key] += ", '" + parts[0][:-1]
                continue

            key = parts[0]
            if key[0] == "'":
                key = key[1:]

            value = parts[1].strip()
            if value[0] == '"' or value[0] == "'":
                value = value[1:-1]
            elif value == "None":
                value = ""
            else:
                value = parseNumber(value)

            itemHash[key] = value

        print('---')
        print(itemHash)
        array.append(itemHash)
        
    return array

    # try:
    #     return json.loads(newJsonStr)
    # except:
    #     print('-------- json that caused ERROR -------')
    #     print(newJsonStr)
    #     raise

with open('../data/credits.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

    i = 0 

    for row in csvreader:
        movieId = row['id']
        castStr = row['cast']
        crewStr = row['crew']

        print(movieId)
        cast = parseJsonStr(castStr)

        i += 1
        if i>2000: break
