#!/usr/local/bin/python3

import csv, json

with open('../data/ratings.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)

    movie_ratings = {}
    for row in csvreader:
        movieId = row['movieId']
        rating = float(row['rating'])
        if movieId not in movie_ratings:
            movie_ratings[movieId] = {
                'rating_sum': rating,
                'count': 1
            }
        else:
            movie_ratings[movieId]['rating_sum'] += rating
            movie_ratings[movieId]['count'] += 1


    print("[")
    for movieId in movie_ratings:
        item = {
            "movieId": movieId,
            "rating": movie_ratings[movieId]['rating_sum']/movie_ratings[movieId]['count']
        }
        print (json.dumps(item) + ",")
    print("]")