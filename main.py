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
        with open(DATABASE) as file:
            try:
                current_db_components = json.load(file)
                print('\n[STATUS] Loading components from JSON.')
                return current_db_components
            except:
                print('\n[ERROR] Unable to load components from JSON.')
               

    def check_file_is_empty(self):
        result = Pipeline.checkFile(DATABASE)
        return result

        # with open(DATABASE) as file:
        #     if file.read() == '':
        #         return False
        #     else:
        #         return True
    
    def check_current_file_date(self):
        result_date = Pipeline.latestFileDate(DATABASE,'07 Sep 2020')
        return result_date

        # with open(DATABASE) as file:
        #     file_date = json.load(file)
        #     file_current_date = file_date.get('07 Sep 2020') #update this

        #     if file_current_date == self.date:
        #         return True
        #     else:
        #         return False
    
    def check_current_id(self): #update this
        u = '1'
        return u
        pass

    def sort_components(self):
        if self.check_current_file_date() == False:
            components = {
                self.date : {
                    'Data' : {
                        self.check_current_id() : {
                            'Location' : self.location,
                            'Items' : self.items,
                            'Prices' : self.prices
                        }
                    }
                }
            }

        if self.check_current_file_date() == True:
            components = {
                self.check_current_id(): {
                    'Location' : self.location,
                    'Items' : self.items,
                    'Prices' : self.prices
                }
            }

        return components
    
    def save_new_component_into_json(self):
        current_db_components = self.retrive_components_from_json()
        new_components = self.sort_components()
        
        try:
            current_db_components.update(new_components)
            to_save_components = current_db_components
            print('\n[STATUS] Succeed updating new components.')

        except:
            print('\n[ERROR] Unable to update new components.')

        finally:
            try:
                with open(DATABASE, 'w') as file:
                    json.dump(to_save_components, file)
                print('\n[STATUS] Succeed overwrite new components into JSON.')
            except:
                print('\n[ERROR] Unable to save components into JSON.')
                print('[WARNING] Components deleted. Please check JSON file.\n')

    def delete_components_from_json(self):
        pass
    
    def search_lists_by_date():
        pass

if __name__ == '__main__':

    location_from_input = 'Jasin'
    items_from_input = 'Food'
    price_from_input = '6.00'

    MainProgram(location_from_input,items_from_input,price_from_input)