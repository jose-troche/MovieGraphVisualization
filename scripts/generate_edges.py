#!/usr/local/bin/python3

import json, random

n = 50000
print ("var edges = [")
for i in range(1, 2*n+1):
    edge = {
        'source': random.randint(0, n-1),
        'target': random.randint(0, n-1)
    }

    print (json.dumps(edge) + ",")
print ("];")