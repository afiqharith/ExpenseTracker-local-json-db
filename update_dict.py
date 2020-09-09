import json

newdict = {
        'location' : 'Jasin',
        'items' : 'Food',
        'total_money' : '5.00'
    }

with open('db.json') as f:
    component = json.load(f)
    component.update(newdict)

    with open('db.json', 'w') as y:
        json.dump(component, y)




print(component)