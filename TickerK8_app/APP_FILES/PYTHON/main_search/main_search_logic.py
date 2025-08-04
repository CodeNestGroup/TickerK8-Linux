import json
import sqlite3
def load_history(self):
    pass
#######################################################################################################################
def text_changed(self):
    _text = self.panel_search_lineedit.text() # Get searching text
    _active_filters = self.global_config['main_search_filters'] # Get filters 
#______________________________________________________________________________________________________________________
    """ Get data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db') # Create connect 
    cursor = database.cursor() # Create cursor
    all_data = []
    if _active_filters[0]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM stock WHERE name like {_text};
        '''))
    elif _active_filters[1]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM etf WHERE name like {_text};
        '''))
    elif _active_filters[2]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM WHERE name like {_text};
        '''))
    elif _active_filters[3]:
        all_data.append(cursor.execute(f'''
            SELECT logo, name, logo, name FROM WHERE name like {_text};
        '''))
    elif _active_filters[4]: 
        all_data.append(cursor.execute(f'''
            SELECT logo, name FROM WHERE name like {_text};
        '''))
    elif _active_filters[5]:
        all_data.append(cursor.execute(f'''
            SELECT icon, name FROM country WHERE name like %{_text}%;
        '''))
#______________________________________________________________________________________________________________________
    """ Set up """
    if self.panel_scroll_widget:
        self.panel_scroll_widget.deleteLater()
        self.panel_scroll_widget = None 
    """ Create widget """
    self.panel_scroll_widget = QWidget(self.panel_scroll)
    self.panel_scroll_widget.setObjectName('panel_scroll_widget')
    self.panel_scroll.setWidget(self.panel_scroll_widget)
    self.panel_scroll_layout = QGridLayout(self.panel_scroll_widget)
    self.panel_scroll_layout.setSpacing(0)
    self.panel_scroll_layout.setContentsMargins(0,0,0,0)
    self.panel_scroll_widget.setLayout(self.panel_scroll_layout)
    for list_object in enumerate(all_data, start=1):
        index_label = QLabel(self.panel_widget)
        object_logo_label = QLabel(self.panel_widget)
        object_name_button = QPushButton(self.panel_widget)
        market_logo_label = QLabel(self.panel_widget)
        market_name_label = QLabel(self.panel_widget)


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