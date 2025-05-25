import json # For json files
import sqlite3 # For local database
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QLabel, # Simple label
    QPushButton, # Simple button
    QScrollArea, # Scroll widget
    QGridLayout, # Grid layout
    QSizePolicy # Size policy 
)
from PyQt5.QtCore import Qt
#######################################################################################################################
""" Statistics country """
def statisitcs_country(self):
    """ Set data """
    database = sqlite3.connect(database=self.main_path+'/CONFIG/GLOBAL/local_data_prototype.db')
    cursor = database.cursor()
    result = cursor.execute(f'SELECT name, flag FROM country WHERE id={self.statistics_object[1]};').fetchall()
#______________________________________________________________________________________________________________________
    """ Set title """
    self.main_title_label.setText(f'{result[0][0]}')
#______________________________________________________________________________________________________________________
    """ Setup widgey """
    if self.scroll_widget: # Check if main scroll have widget 
        self.scroll_widget.deleteLater() # Delete scroll widget
        self.scroll_widget = None # Set dafault 
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.scroll_widget = QWidget(self.main_scroll)
    self.scroll_layout = QGridLayout(self.scroll_widget)
    self.gdp_button = QPushButton(self.scroll_widget)
    self.n_r_button = QPushButton(self.scroll_widget)
    self.people_button = QPushButton(self.scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.scroll_widget.setObjectName('scroll_widget')
    self.gdp_button.setObjectName('gdp_button')
    self.n_r_button.setObjectName('n_r_button')
    self.people_button.setObjectName('people_button')
#______________________________________________________________________________________________________________________
    """ Set property """
    self.gdp_button.setProperty('class', 'option_button')
    self.n_r_button.setProperty('class', 'option_button')
    self.people_button.setProperty('class', 'option_button')
#______________________________________________________________________________________________________________________
    """ Set layout """
    self.scroll_layout.addWidget(self.gdp_button, 0, 0)
    self.scroll_layout.addWidget(self.n_r_button, 0, 1)
    self.scroll_layout.addWidget(self.people_button, 1, 0)
    self.scroll_layout.setSpacing(0)
    self.scroll_layout.setContentsMargins(0,0,0,0)
    self.scroll_widget.setLayout(self.scroll_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    #self.main_scroll.setWidget(self.scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set size """
    self.scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.gdp_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.n_r_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    self.people_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Set graphics """
    self.gdp_button.setText('A')
    self.n_r_button.setText('B')
    self.people_button.setText('C')
    self.main_scroll.setWidget(self.scroll_widget)
#______________________________________________________________________________________________________________________
    """ Set connect """
    self.gdp_button.clicked.connect(open_gdp)
    self.n_r_button.clicked.connect(open_n_r)
    self.people_button.clicked.connect(open_people)
#######################################################################################################################
""" Statistics market """
def statisitcs_market(self):
    pass
#######################################################################################################################
""" Statistics index """
def statisitcs_index(self):
    pass
#######################################################################################################################
""" Statistics stock """
def statisitcs_stock(self):
    pass
#######################################################################################################################
""" Open gdp """
def open_gdp(self):
    pass
#######################################################################################################################
""" Open natural resources """
def open_n_r(self):
    if self.scroll_widget: # Check if main scroll has widget 
        self.scroll_widget.deleteLater() # Delete widget 
        self.scroll_widget = None  # Set dafault 
#######################################################################################################################
""" Open people """
def open_people(self):
    pass
#######################################################################################################################