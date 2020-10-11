__author__ = "Afiq Harith"
__email__ = "afiqharith05@gmail.com"
__date__ = "09 Sep 2020"
__status__ = "Development"

'''
1. check date on json
2. check id on json
3. update self id on json

'''

import json
from datetime import datetime
from pipeline import Pipeline

DATABASE = 'db.json'
current = datetime.now()

class MainProgram:
    def __init__ (self,location, items, prices, program_status = True):
        self.location = location
        self.items = items
        self.prices = prices
        self.date = current.strftime("%d %b %Y")
        self.program_status = program_status
        
        if self.program_status == True:
            self.save_new_component_into_json()

    def retrive_components_from_json(self):
        return Pipeline.GetFromFile(DATABASE)
        
    def check_file_is_empty(self):
        return Pipeline.checkFile(DATABASE)

    def check_current_file_date(self):
        return Pipeline.latestFileDate(DATABASE,'07 Sep 2020')
    
    def check_current_id(self): #update this
        u = '1'
        return u
        pass

    def sort_components(self):
        if self.check_current_file_date() == False:
            components = Pipeline.CompoSortWithDate(self.date, self.check_current_id(), self.location, self.items, self.prices)

        if self.check_current_file_date() == True:
            components = Pipeline.CompoSortNoDate(self.check_current_id(), self.location, self.items, self.prices)
        return components
    
    def save_new_component_into_json(self):
        current_db_components = self.retrive_components_from_json()
        new_components = self.sort_components()
        current_db_components.update(new_components)
        to_save_components = current_db_components

        with open(DATABASE, 'w') as file:
            json.dump(to_save_components, file)


    def delete_components_from_json(self):
        pass
    
    def search_lists_by_date():
        pass

if __name__ == '__main__':

    location_from_input = 'Jasin'
    items_from_input = 'Food'
    price_from_input = '6.00'

    MainProgram(location_from_input,items_from_input,price_from_input)