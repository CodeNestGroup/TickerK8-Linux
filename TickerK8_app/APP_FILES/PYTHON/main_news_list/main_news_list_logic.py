""" Import """
import mysql
import json
#______________________________________________________________________________________________________________________
""" Import PyQt5 Widgets """
from PyQt5.QtWidgets import (
    QWidget, # Simple widget, window
    QPushButton, # Simple button
    QLabel, # Label
    QGridLayout, # Grid layout
    QSizePolicy, # Size policy
    QVBoxLayout, # Vertical layout 
    QSizePolicy # Size policy 
)
#______________________________________________________________________________________________________________________
""" Import PyQt5 Core """
from PyQt5.QtCore import (
    Qt, # Qt settings
    QSize # Size
)
#######################################################################################################################
""" News main widget """
def news_main_widget(self):
    """ Load user settings """
    user_setting = dict(json.load(open(self.main_path+'/CONFIG/GLOBAL/logged_user.json', 'r'))).keys()[self.news_type]
    news_type_name = None # Set dafoult
    if self.news_type == 0:
        news_type_name = 'market'
    elif self.news_type == 1:
        news_type_name = 'country'
    else:
        news_type_name = 'world'
#______________________________________________________________________________________________________________________
    """ Get data """
    connect = mysql.connector.connect(
        host = "localhost",
        user = "client",
        password = "Qwerty123456#",
        database = "TickerK8"
    )
    cursor = connect.cursor()
    cursor.execute(f'SELECT title, date  FROM news WHERE {news_type_name}={user_setting};')
    json_file = json.loads(cursor.fetchall()[0][0])
#______________________________________________________________________________________________________________________
    """ Create objects """
    self.news_widget = QWidget(self.news_list_scroll)
    self.news_layout = QVBoxLayout(self.news_widget)
#______________________________________________________________________________________________________________________
    """ Set object name """
    self.news_widget.setObjectName('news_widget')
#______________________________________________________________________________________________________________________
    """ Set property """
#______________________________________________________________________________________________________________________
    """ Set Layout """
    self.news_layout.setSpacing(0)
    self.news_layout.setContentsMargins(0,0,0,0)
    self.news_widget.setLayout(self.news_layout)
#______________________________________________________________________________________________________________________
    """ Set widget """
    self.news_scroll.setWidget(self.news_wdidget)
#______________________________________________________________________________________________________________________
    """ Set label """
#______________________________________________________________________________________________________________________
    """ Set size """
    self.news_widget.setMaximumWidth(self.news_list_scroll.width())
    self.news_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
#______________________________________________________________________________________________________________________
    """ Make news widget content """
    for index, rows in enumerate(json_file, start=0):
        pass
#######################################################################################################################
