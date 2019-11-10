#!/usr/local/bin/python3

# Parses credits.csv and converts it to json

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
        # print('===')
        # print(item)
        itemHash = {}
        for pair in item.split(", '"):
            #print('+++')
            #print(pair)
            parts = pair.split("': ")

            partsLength = len(parts)

            if (partsLength < 2):
                itemHash[key] += ", '" + parts[0][:-1]
                continue

            key = parts[0]
            if key[0] == "'":
                key = key[1:]

            if (partsLength == 3):
                value = "': " + parts[2].strip()
            else:
                value = parts[1].strip()
            
            if value[0] == '"' or value[0] == "'":
                value = value[1:-1]
            elif value == "None":
                value = ""
            else:
                value = parseNumber(value)

            itemHash[key] = value

        # print('---')
        # print(itemHash)
        array.append(itemHash)
        
    return array

with open('../data/credits.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

    i = 0

    print("[")

    for row in csvreader:
        movieId = row['id']
        castStr = row['cast']
        crewStr = row['crew']

        cast = parseJsonStr(castStr)
        crew = parseJsonStr(crewStr)

        record = {
            'movieId': movieId,
            'cast': cast,
            'crew': crew
        }

        print(json.dumps(record) + ",")

        i += 1
        #print(i)
        #if i>2: break

    print("]")
