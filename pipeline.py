import json
from datetime import datetime
current = datetime.now()
CURRENT_DATE = current.strftime("%d %b %Y")

class Pipeline(object):

    '''
    [usage]:
    checkFile(param='json file name')
    '''
    def checkFile(DATABASE):
        with open(DATABASE) as file:
            if file.read() == '':
                return False
            else:
                return True
    
    '''
    [usage]:
    latestFileDate([param='json file name'], [param2=desired date])
    '''
    def latestFileDate(DATABASE,DATE):
        with open(DATABASE) as file:
            if json.load(file).get(DATE) == CURRENT_DATE:
                return True 
            else: 
                return False

    def componentsSort(ID,DATE,LOCATION,ITEMS,PRICES,STAT):
        if STAT == False:
            components = { DATE : { 'Data' : { ID : { 'Location' : LOCATION, 'Items' : ITEMS, 'Prices' : PRICES }}}}
        if STAT == True:
            components = { ID : { 'Location' : LOCATION, 'Items' : ITEMS, 'Prices' : PRICES }}
        return components
