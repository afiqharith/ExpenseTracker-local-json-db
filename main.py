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

current = datetime.now()
current_date = current.strftime("%d %b %Y")

class MainProgram():
    def __init__ (self,location, items, prices, date,program_status):
        self.location = location
        self.items = items
        self.prices = prices
        self.date = date
        self.program_status = program_status
        
        if self.program_status == True:
            self.start_main_program()

    def retrive_components_from_json(self):
        with open('db.json') as file:
            try:
                current_db_components = json.load(file)
                print('\n[STATUS] Loading components from JSON.')
                return current_db_components
            except:
                print('\n[ERROR] Unable to load components from JSON.')
               

    def check_file_is_empty(self):
        with open('db.json') as file:
            if file.read() == '':
                return False
            else:
                return True
    
    def check_current_file_date(self):
        with open('db.json') as file:
            file_date = json.load(file)
            file_current_date = file_date.get('07 Sep 2020') #update this

            if file_current_date == current_date:
                return True
            else:
                return False
    
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
                with open('db.json', 'w') as file:
                    json.dump(to_save_components, file)
                print('\n[STATUS] Succeed overwrite new components into JSON.')
            except:
                print('\n[ERROR] Unable to save components into JSON.')
                print('[WARNING] Components deleted. Please check JSON file.\n')

    def delete_components_from_json(self):
        pass
    
    def search_lists_by_date():
        pass

    def start_main_program(self):
        self.save_new_component_into_json()
        # self.retrive_components_from_json()
        pass


def main():
    location_from_input = 'Jasin'
    items_from_input = 'Food'
    price_from_input = '6.00'

    MainProgram(location_from_input,items_from_input,price_from_input,current_date, program_status = True)
   

if __name__ == '__main__':
    main()