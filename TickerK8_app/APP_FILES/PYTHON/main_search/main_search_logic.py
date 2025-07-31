import json
import sqlite3
def load_history(self):
    pass
#######################################################################################################################
def text_changed(self):
    _text = self.panel_search_lineedit.text() # Get searching text
    _active_filters = self.global_config['main_search_filters'] # Get filters 
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor 
    country_data = cursor.execute(f'''
    SELECT FROM WHERE name like {_text};
    ''')

#######################################################################################################################
def filters_changed(self, index):
    self.global_config['main_search_filters'][index] = not self.global_config['main_search_filters'][index] # Change
    json.dump(self.global_config, open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'w'), indent=4) # Save 
    self.global_config = json.load(open(self.main_path+'/CONFIG/GLOBAL/global_config.json', 'r')) # Reload
    filters_load(self)
#######################################################################################################################
def filters_load(self):
    _active_filters = self.global_config['main_search_filters']
    for index, f in enumerate(_active_filters, start=0):
        if f:
            self.button_list[index].setStyleSheet('background-color: #031913;')
        else:
            self.button_list[index].setStyleSheet('background-color: #252525;')

#######################################################################################################################