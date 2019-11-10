#!/usr/local/bin/python3

import json

n = 50000
print ("var nodes = [")
for i in range(1, n+1):
    node = {
        'id': i,
        'label': "Node"+str(i),
        'group': i%2
    }

    print (json.dumps(node) + ",")
print ("];")