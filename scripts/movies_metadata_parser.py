#!/usr/local/bin/python3

# Parses movie_metadata.csv and converts it to json

import csv, json, re

itemRegex = re.compile(r'\{(.*?)\}')

def parseNumber(s):
    if s == '' or s is None:
        return 0
    try:
        return int(s)
    except ValueError:
        return float(s)

def parseJsonStr(jsonStr):
    array = []

    if jsonStr == '' or jsonStr is None:
        return array

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

with open('../data/movies_metadata.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

    i = 0

    print("[")

    for row in csvreader:
        #print(row)

        record = {}

        try:
            record['adult'] = True if row['adult'] == 'True' else False
            record['belongs_to_collection'] = parseJsonStr(row['belongs_to_collection'])
            record['budget'] = parseNumber(row['budget'])
            record['genres'] = parseJsonStr(row['genres'])
            record['homepage'] = row['homepage']
            record['id'] = row['id']
            record['imdb_id'] = row['imdb_id']
            record['original_language'] = row['original_language']
            record['original_title'] = row['original_title']
            record['overview'] = row['overview']
            record['popularity'] = parseNumber(row['popularity'])
            record['poster_path'] = row['poster_path']
            record['production_companies'] = parseJsonStr(row['production_companies'])
            record['production_countries'] = parseJsonStr(row['production_countries'])
            record['release_date'] = row['release_date']
            record['revenue'] = parseNumber(row['revenue'])
            record['runtime'] = parseNumber(row['runtime'])
            record['spoken_languages'] = parseJsonStr(row['spoken_languages'])
            record['status'] = row['status']
            record['tagline'] = row['tagline']
            record['title'] = row['title']
            record['video'] = True if row['video'] == 'True' else False
            record['vote_average'] = parseNumber(row['vote_average'])
            record['vote_count'] = parseNumber(row['vote_count'])
        except:
            print('Error when converting row')
            print(row)
            raise

        print(json.dumps(record) + ",")

        i += 1
        #print(i)
        #if i>20: break

    print("]")
