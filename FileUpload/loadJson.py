# JSON - Javascript Object Notation
# Lightweight
import json

# json.load()
# json.loads()
#
# json.dump()
# json.dumps()

with open('data.json') as data_file:
    data = json.load(data_file)
    for row in data:
        print(row)